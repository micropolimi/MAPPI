# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 13:00:05 2020

@authors: Alberto Ghezzi, Andrea Bassi. Politecnico di Milano
"""
from simple_pyspin import Camera

class FlirDevice(object):
    '''
    Scopefoundry compatible class to run a FLIR camera with spinnaker software
    For Pointgrey grasshopper, the bit depth is 16bit or 8bit, specified in the PixelFormat attribute, 
    simple_pyspin is not compatible with 12bit readout. 
    '''
    
    def __init__(self, camera_num=0, serial = 'unavailable', debug=False, dummy=False):
        self.debug = debug
        self.dummy = dummy
        
        if not self.dummy:
            if serial =='unavailable':
                self.cam = Camera(camera_num)
            else:
                self.cam = Camera(serial)
            self.cam.init()
            self.cam.ExposureAuto = 'Off'
            self.cam.ExposureMode = 'Timed'
            self.cam.GainAuto = 'Off'
            self.cam.AcquisitionFrameRateEnabled = True
            self.cam.AcquisitionFrameRateAuto = 'Off' 
            self.cam.AutoFunctionAOIsControl = 'Off'
            self.cam.AcquisitionMode = 'Continuous'
            self.cam.ChunkEnable = False
            self.cam.EventNotification = 'Off'
            self.cam.GammaEnabled = False
            self.cam.PixelFormat = 'Mono16' # specify here the bit depth
            self.cam.BlackLevel = 1.0 # 
            self.cam.TriggerMode = 'Off'
            self.cam.OnBoardColorProcessEnabled = False
            
    def set_acquisitionmode(self,mode):
        self.cam.AcquisitionMode = mode
        
    def get_acquisitionmode(self):
        mode = self.cam.AcquisitionMode
        return(mode)
    
    def close(self):
        self.cam.close()
        
    def set_framenum(self, Nframes):
        if self.cam.AcquisitionMode == 'MultiFrame': 
            self.cam.AcquisitionFrameCount = Nframes 
                    
    def read_temperature(self):
        resp = self.cam.DeviceTemperature
        return resp   
    
    def get_width(self):
        w = self.cam.Width
        return w    
    
    def get_height(self):
        h = self.cam.Height
        return h      
    
    def acq_start(self):
        self.cam.start()
    
    def get_nparray(self):
        return self.cam.get_array()
    
    def acq_stop(self):
        self.cam.stop()  
    
    def get_exposure(self):
        "get the exposure time in ms"
        return self.cam.ExposureTime/1000

    def set_exposure(self, desired_time):
        "set the exposure time in ms"
        maxexp = self.cam.get_info('ExposureTime')['max'] 
        minexp = self.cam.get_info('ExposureTime')['min']
        exptime = min(maxexp, max(desired_time*1000, minexp))
        self.cam.ExposureTime = exptime
    
    def get_rate(self):
        return self.cam.AcquisitionFrameRate

    def set_rate(self, desired_framerate):
        """ Set the framerate in Hz
            FLIR Grasshopper runs at:
            163.57 fps at 8bit, full frame
            87.08 fps at 12 bit, not supported by simple_pyspin
            82.47 fps at 16bit is used here
        """
        maxfr = self.cam.get_info('AcquisitionFrameRate')['max'] 
        minfr = self.cam.get_info('AcquisitionFrameRate')['min']
        framerate = max(minfr, min(desired_framerate, maxfr))
        self.cam.AcquisitionFrameRate = framerate
    
    def get_gain(self):
        return self.cam.Gain    
    
    def set_gain(self, desired_gain):
        "set the gain in dB"
        maxgain = self.cam.get_info('Gain')['max'] 
        self.cam.Gain = min(desired_gain,maxgain)
        
    def get_idname(self):
        cam_name = self.cam.DeviceVendorName.strip() + ' ' + self.cam.DeviceID.strip() + ' ' + self.cam.DeviceModelName.strip() 
        return cam_name
    
    def get_serial(self):
        cam_serial = self.cam.DeviceSerialNumber
        return cam_serial
        
if __name__ == '__main__':
    
    try:    
        camera = FlirDevice()
        camera.set_acquisitionmode('Continuous')
        camera.acq_start()
        im = camera.get_nparray()
        camera.acq_stop() 
        
        print("Acquired image shape:", im.shape)
        
    except Exception as err:
        print(err)
    
    finally:
        camera.close()