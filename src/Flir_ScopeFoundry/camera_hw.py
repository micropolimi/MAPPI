# -*- coding: utf-8 -*-
"""
Created on Mar 20 12:45:26 2024

@authors: Andrea Bassi. Politecnico di Milano
"""
from ScopeFoundry import HardwareComponent
from camera_device import FlirDevice

class FlirHW(HardwareComponent):
    name = 'FLIRhw'
    
    def setup(self):
        # create Settings (aka logged quantities)  
        self.infos = self.settings.New(name='name', dtype=str)
        self.camera_number = self.settings.New(name='number', dtype=int, initial = 0)
        self.camera_serial = self.settings.New(name='serial', dtype=str, initial = 'unavailable')
        self.image_width = self.settings.New(name='image_width', dtype=int, ro=True,unit='px')
        self.image_height = self.settings.New(name='image_height', dtype=int, ro=True,unit='px')
        
        self.frame_rate = self.settings.New(name='frame_rate', initial= 9,
                                            vmax = 1000., vmin = 0.01, spinbox_step = 0.1,
                                            unit = 'fps',dtype=float, ro=False, reread_from_hardware_after_write=True)
        self.exposure_time = self.settings.New(name='exposure_time', initial=100, vmax =5000.,
                                               vmin = 0.01, spinbox_step = 0.1,dtype=float, ro=False, unit='ms',reread_from_hardware_after_write=True)
        self.frame_num = self.settings.New(name='frame_num',initial= 10, spinbox_step = 1,
                                           dtype=int, ro=False)
        self.acquisition_mode = self.settings.New(name='acquisition_mode', dtype=str,
                                                  choices=['Continuous', 'MultiFrame'], initial = 'Continuous', ro=False)
        self.gain = self.settings.New(name='gain', initial=0., dtype=float,
                                      vmax = 1000., vmin = 0., spinbox_step = 1.,
                                      ro=False, unit='dB', reread_from_hardware_after_write=True)
        self.temperature = self.settings.New(name='temperature', dtype=float, ro=True, unit=chr(176)+'C' )
        
    def connect(self):
        # create an instance of the Device
        self.camera = FlirDevice(serial=self.camera_serial.val, debug=self.debug_mode.val)      
        # connect settings to Device methods
        self.temperature.hardware_read_func = self.camera.read_temperature
        self.image_width.hardware_read_func = self.camera.get_width
        self.image_height.hardware_read_func = self.camera.get_height
        self.infos.hardware_read_func = self.camera.get_idname
        self.exposure_time.hardware_read_func = self.camera.get_exposure
        self.exposure_time.hardware_set_func = self.camera.set_exposure
        self.frame_rate.hardware_read_func = self.camera.get_rate
        self.frame_rate.hardware_set_func = self.camera.set_rate
        self.acquisition_mode.hardware_set_func = self.camera.set_acquisitionmode
        self.frame_num.hardware_set_func = self.camera.set_framenum
        self.gain.hardware_read_func = self.camera.get_gain
        self.gain.hardware_set_func = self.camera.set_gain
        self.camera_serial.hardware_read_func = self.camera.get_serial
        self.debug_mode.hardware_read_func = self.camera.get_debug_mode
        self.debug_mode.hardware_set_func = self.camera.set_debug_mode
        self.read_from_hardware()
        
    def disconnect(self):
        if hasattr(self, 'camera'):
            self.camera.close() 
            del self.camera
            
        for lq in self.settings.as_list():
            lq.hardware_read_func = None
            lq.hardware_set_func = None

