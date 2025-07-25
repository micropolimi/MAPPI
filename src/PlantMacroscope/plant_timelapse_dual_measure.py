# -*- coding: utf-8 -*-
"""
Created on Mar 20 12:45:26 2024

@authors: Andrea Bassi. Politecnico di Milano
"""
from ScopeFoundry import Measurement
from ScopeFoundry.helper_funcs import sibling_path, load_qt_ui_file
from ScopeFoundry import h5_io
import pyqtgraph as pg
import numpy as np
import os
import time

VIEWS = {'Y':0, 'X':1}

class PlantTimeLapseDualMeasure(Measurement):

    name = "PlantTimeLapseDualMeasure"

    def setup(self):
        """
        Runs once during App initialization.
        This is the place to load a user interface file,
        define settings, and set up data structures.
        For Pointgrey Grasshopper CMOS the pixelsize is: 5.86um
        """

        self.ui_filename = sibling_path(__file__, "camera.ui")
        self.ui = load_qt_ui_file(self.ui_filename)
        self.settings.New('camera_in_use', dtype=str, choices=list(VIEWS), initial=list(VIEWS)[0])
        self.settings.New('acquisition_time', dtype=float, unit='ms',
                          initial=100.0, spinbox_decimals=3, vmin=0.01)
        self.settings.New('time_lapse_num', dtype=int, initial=1, vmin=1)
        self.settings.New('time_lapse_waiting_time', dtype=float, unit='s',
                          initial=5.0, spinbox_decimals=3)
        self.settings.New('frame_num',dtype=int,initial=1,vmin=1)
        self.settings.New('LED_init_time', dtype=float, unit='s',
                          initial=0.0, spinbox_decimals=3)
        self.settings.New('xsampling', dtype=float, unit='um',
                          initial=0.058, spinbox_decimals=3)
        self.settings.New('ysampling', dtype=float, unit='um',
                          initial=0.058, spinbox_decimals=3)
        self.settings.New('zsampling', dtype=float, unit='um',
                          initial=1.0, spinbox_decimals=4)
        self.auto_range = self.settings.New('auto_range', dtype=bool, initial=True)
        self.settings.New('auto_levels', dtype=bool, initial=True)
        self.settings.New('level_min', dtype=int, initial=60)
        self.settings.New('level_max', dtype=int, initial=4000)
        self.settings.New('save_h5', dtype=bool, initial=False)
        self.settings.New('refresh_period', dtype=float,
                          unit='s', spinbox_decimals=3, initial=0.03, vmin=0)
        
        self.setup_hardware()

    def set_view(self,view='X'):
        if hasattr(self, 'cameras'):
            cam = self.cameras[VIEWS[view]]
            acq_time = cam.settings['exposure_time']
            self.settings['acquisition_time'] = acq_time
    
    def set_acq_time(self, desired_time):
        if hasattr(self, 'cameras'):
            view = self.settings['camera_in_use']
            cam_idx = VIEWS[view]
            cam = self.cameras[cam_idx]
            # maxfr = cam.camera.cam.get_info('AcquisitionFrameRate')['max'] 
            # minfr = cam.camera.cam.get_info('AcquisitionFrameRate')['min']
            # desired_rate = 1000/desired_time * 0.95 # consider 5% less than maximum achievable
            desired_rate = 1.0 #TODO: fix the syncronization bug
            cam.settings['frame_rate'] = desired_rate
            # fr = cam.camera.cam.AcquisitionFrameRate
            maxexp = cam.camera.cam.get_info('ExposureTime')['max']/1000.0
            cam.settings['exposure_time'] = desired_time
            if desired_time > maxexp:
                print(f'Warning: desiderd exposure time {desired_time} exceeds maximun time {maxexp}')
            
            
    def setup_hardware(self):
        self.cameras = []
        self.leds = []
        
        cam = self.app.hardware['camera_y']
        self.cameras.append(cam)
        
        self.leds.append(self.app.hardware['led_y'])
        self.app.hardware['led_y'].channel_1.connect_to_widget(self.ui.led_y_Box)
        
        cam = self.app.hardware['camera_x']
        self.cameras.append(cam)
        
        self.leds.append(self.app.hardware['led_x'])   
        self.app.hardware['led_x'].channel_1.connect_to_widget(self.ui.led_x_Box)
        
        for c in self.cameras:
            c.read_from_hardware()
            
            
    def setup_figure(self):
        """
        Runs once during App initialization, after setup()
        This is the place to make all graphical interface initializations,
        build plots, etc.
        """

        # connect ui widgets to measurement/hardware settings or functions
        self.ui.start_pushButton.clicked.connect(self.start)
        self.ui.interrupt_pushButton.clicked.connect(self.interrupt)
        self.settings.save_h5.connect_to_widget(self.ui.save_h5_checkBox)
        self.settings.auto_levels.connect_to_widget(
            self.ui.autoLevels_checkbox)
        self.settings.auto_range.connect_to_widget(self.ui.autoRange_checkbox)
        self.settings.level_min.connect_to_widget(self.ui.min_doubleSpinBox)
        self.settings.level_max.connect_to_widget(self.ui.max_doubleSpinBox)
        self.settings.time_lapse_num.connect_to_widget(self.ui.num_Box)
        self.settings.time_lapse_waiting_time.connect_to_widget(self.ui.waiting_timeBox)
        self.settings.camera_in_use.connect_to_widget(self.ui.viewBox)
        self.settings.acquisition_time.connect_to_widget(self.ui.acquisitionBox)
        self.settings.camera_in_use.hardware_set_func = self.set_view
        self.settings.acquisition_time.hardware_set_func = self.set_acq_time
        
        # Set up pyqtgraph graph_layout in the UI
        self.imv = pg.ImageView()
        self.ui.imageLayout.addWidget(self.imv)
        colors = [(0, 0, 0),
                  (45, 5, 61),
                  (84, 42, 55),
                  (150, 87, 60),
                  (208, 171, 141),
                  (255, 255, 255)
                  ]
        cmap = pg.ColorMap(pos=np.linspace(0.0, 1.0, 6), color=colors)
        self.imv.setColorMap(cmap)

    def update_display(self):
        """
        Displays (plots) the numpy array self.buffer. 
        This function runs repeatedly and automatically during the measurement run.
        its update frequency is defined by self.display_update_period
        """
        self.display_update_period = self.settings['refresh_period']
        length = self.settings['time_lapse_num']

        self.settings['progress'] = (self.time_index + 1) * 100/length

        if hasattr(self, 'img'):
            self.imv.setImage(self.img.T,
                              autoLevels=self.settings['auto_levels'],
                              autoRange=self.auto_range.val,
                              levelMode='mono'
                              )

            if self.settings['auto_levels']:
                lmin, lmax = self.imv.getHistogramWidget().getLevels()
                self.settings['level_min'] = lmin
                self.settings['level_max'] = lmax
            else:
                self.imv.setLevels(min=self.settings['level_min'],
                                   max=self.settings['level_max'])

    def measure(self):
        """
        Set mode to Multiframe, acquire Nframes frames and eventually save them in h5 
        """
        self.images = []
        
        time_lapse_num = self.settings['time_lapse_num'] 
        time_lapse_waiting_time = self.settings['time_lapse_waiting_time']
        frame_num = self.settings.frame_num.val
        
        for c in self.cameras:
            #c.camera.acq_stop()
            c.settings['acquisition_mode'] = 'MultiFrame'
            c.settings['frame_num'] = frame_num+1 #note that we acquire and than skip the first frame
            c.read_from_hardware()
        
        self.initial_time = time.time()
        
        for time_lapse_idx in range(time_lapse_num):
            self.time_index = time_lapse_idx
            if self.interrupt_measurement_called:
                break
            
            for L in self.leds:
                L.turn_on()
                L.read_from_hardware()
            time.sleep(self.settings['LED_init_time']) # waiting time to turn on the LED
            first_frame_acquired = False
            for c in self.cameras:
                c.camera.acq_start()
                
            self.images = []
            
            for frame_idx in range(frame_num+1): #note that we acquire and than skip the first frame
                
                self.frame_index = frame_idx
                for cam_idx,cam in enumerate(self.cameras):
                    img = cam.camera.get_nparray() #TODO: syncro bug make sure that the image has been acquired before getting it
                    # print('acq time:', time.time() - self.initial_time)
                    if first_frame_acquired:
                        self.images[cam_idx] = img
                    else:
                        self.images.append(img) 
                    if cam == self.cameras[VIEWS[self.settings['camera_in_use']]]:
                        self.img = img             
                if self.settings['save_h5']:
                    if not first_frame_acquired:
                        if time_lapse_idx == 0:
                            self.create_h5_file()
                        else:
                            self.init_h5_dataset(time_lapse_idx)
                        first_frame_acquired = True
                    for cam_idx,cam in enumerate(self.cameras):
                        self.h5_datasets[cam_idx][frame_idx-1, :, :] = self.images[cam_idx] # #note that we acquire and than skip the first frame
               
                    self.h5file.flush()

                if self.interrupt_measurement_called:
                    break
            
            for c in self.cameras:
                c.camera.acq_stop()
            for L in self.leds:
                L.turn_off()
                L.read_from_hardware()
            # wait for next time lapse measurement
            while time.time()<self.initial_time+(time_lapse_idx+1)*time_lapse_waiting_time:
                if self.interrupt_measurement_called:
                    break

    def run(self):
        """
        Runs when measurement is started. Runs in a separate thread from GUI.
        It should not update the graphical interface directly, and should only
        focus on data acquisition.
        
        """
        
        for c in self.cameras:
            c.read_from_hardware()
            
        self.settings['camera_in_use'] = 'X'
        self.settings['camera_in_use'] = 'Y'

        try:
            self.frame_index = -1
            self.time_index = -1
            for c in self.cameras:
                c.settings['acquisition_mode'] = 'Continuous'
                c.camera.acq_start()

            while not self.interrupt_measurement_called:
                c = self.cameras[VIEWS[self.settings['camera_in_use']]]
                self.img = c.camera.get_nparray()

                if self.interrupt_measurement_called:
                    break

                if self.settings['save_h5']:
                    # measure is triggered by save_h5 button
                    for c in self.cameras:
                        c.camera.acq_stop()
                    self.measure()
                    break

        finally:
            for c in self.cameras:
                c.camera.acq_stop()
            if self.settings['save_h5'] and hasattr(self, 'h5file'):
                # make sure to close the data file
                self.h5file.close()

    def create_saving_directory(self):
        if not os.path.isdir(self.app.settings['save_dir']):
            os.makedirs(self.app.settings['save_dir'])

    def create_h5_file(self):
        self.create_saving_directory()
        # file name creation
        timestamp = time.strftime("%y%m%d_%H%M%S", time.localtime())
        sample = self.app.settings['sample']
        #sample_name = f'{timestamp}_{self.name}_{sample}.h5'
        if sample == '':
            sample_name = '_'.join([timestamp, self.name])
        else:
            sample_name = '_'.join([timestamp, self.name, sample])
        fname = os.path.join(
            self.app.settings['save_dir'], sample_name + '.h5')

        self.h5file = h5_io.h5_base_file(
            app=self.app, measurement=self, fname=fname)
        self.h5_group = h5_io.h5_create_measurement_group(
            measurement=self, h5group=self.h5file)
        self.init_h5_dataset(time_idx=0)


    def init_h5_dataset(self,time_idx):
        img_size = self.img.shape
        dtype = self.img.dtype
        actual_time = time.time()-self.initial_time
        print('measurement:', time_idx, 'at time:', actual_time)
        length = self.settings.frame_num.val
        self.h5_datasets = []
        for c_idx,c in enumerate(self.cameras):
            name = f't{time_idx:04d}/c{c_idx}/image'
            dataset = self.h5_group.create_dataset(name=name,
                                                    shape=[length, img_size[0], img_size[1]],
                                                    dtype=dtype)
            dataset.attrs['view'] = c_idx
            dataset.attrs['time_idx'] = time_idx
            dataset.attrs['acquisition_time'] = actual_time
            dataset.attrs['frame_interval_s'] = self.settings['time_lapse_waiting_time']
            dataset.attrs['element_size_um'] = [self.settings['zsampling'],
                                                self.settings['ysampling'],
                                                self.settings['xsampling']]
            self.h5_datasets.append(dataset)