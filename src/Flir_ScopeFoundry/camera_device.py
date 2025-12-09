# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 13:00:05 2020

@authors: Alberto Ghezzi, Andrea Bassi. Politecnico di Milano
"""
from simple_pyspin import Camera
import PySpin

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
            
    def set_debug_mode(self, value):
        self.debug = value

    def get_debug_mode(self):
        return self.debug
    
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
        if self.debug:
            import time
            print('Acquistion started at time:', time.time())
    
    def get_nparray(self):
        return self.cam.get_array()
    
    def acq_stop(self):
        self.cam.stop()  
    
    def get_exposure(self):
        "get the exposure time in ms"
        val = self.cam.ExposureTime/1000
        if self.debug:
            maxexp = self.cam.get_info('ExposureTime')['max']/1000 
            minexp = self.cam.get_info('ExposureTime')['min']/1000
            print (f'Exposure: {val} with min: {minexp} and max: {maxexp}') 
        return val
    

    def set_exposure(self, desired_time):
        "set the exposure time in ms"
        maxexp = self.cam.get_info('ExposureTime')['max'] 
        minexp = self.cam.get_info('ExposureTime')['min']
        exptime = min(maxexp, max(desired_time*1000, minexp))
        self.cam.ExposureTime = exptime
    
    def get_rate(self):
        val = self.cam.AcquisitionFrameRate
        
        if self.debug:
            maxfr = self.cam.get_info('AcquisitionFrameRate')['max'] 
            minfr = self.cam.get_info('AcquisitionFrameRate')['min']
            print(f'Acquisition rate: {val} with min: {minfr} and max: {maxfr}')  
        return val

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
        
    
    def get_acquisition_mode(self):
        nodemap = self.cam.cam.GetNodeMap()
        val = PySpin.CEnumerationPtr(nodemap.GetNode('AcquisitionMode'))
        val_str = val.ToString()
        if self.debug:
            print(f'{val.GetName()}: {val_str}')
        return(val_str)
    
    def get_stream_mode(self):
        nodemap_tlstream = self.cam.cam.GetTLStreamNodeMap()
        val = PySpin.CEnumerationPtr(nodemap_tlstream.GetNode('StreamBufferHandlingMode'))
        val_str = val.ToString()
        if self.debug:
            print(f'{val.GetName()}: {val_str}')
        return(val_str)
    
    def get_buffer_count(self):
        nodemap_tlstream = self.cam.cam.GetTLStreamNodeMap()
        val = PySpin.CIntegerPtr(nodemap_tlstream.GetNode('StreamDefaultBufferCount'))
        if PySpin.IsReadable(val):
            val_str = val.ToString()
            if self.debug:
               print(f'{val.GetName()}:val_str')
            return(val)
        else:
            print('Buffer count not readable')
            return
    
        
    def set_stream_mode(self, buffer_count=10, buffer_mode='NewestOnly'):
        """Configure image buffer handling: Set mode to OldestFirst or NewestOnly"""
        try:
            # Get transport layer stream nodemap
            nodemap_tlstream = self.cam.cam.GetTLStreamNodeMap()
    
            # Set buffer count
            node_buffer_count = PySpin.CIntegerPtr(nodemap_tlstream.GetNode('StreamDefaultBufferCount'))
            if PySpin.IsReadable(node_buffer_count) and PySpin.IsWritable(node_buffer_count):
                node_buffer_count.SetValue(buffer_count)
                print(f'Buffer count set to: {buffer_count}')
    
            # Set buffer handling mode
            node_buffer_mode = PySpin.CEnumerationPtr(nodemap_tlstream.GetNode('StreamBufferHandlingMode'))
            if PySpin.IsReadable(node_buffer_mode) and PySpin.IsWritable(node_buffer_mode):
                node_buffer_mode_entry = node_buffer_mode.GetEntryByName(buffer_mode)
                if PySpin.IsReadable(node_buffer_mode_entry):
                    buffer_mode_value = node_buffer_mode_entry.GetValue()
                    node_buffer_mode.SetIntValue(buffer_mode_value)
                    print(f'Buffer handling mode set to: {buffer_mode}')
    
            return True
    
        except PySpin.SpinnakerException as ex:
            print(f'Error configuring buffer handling: {ex}')
            return False
    
    
    
    
    
    
    
if __name__ == '__main__':
    
   
        camera = FlirDevice()
        camera.set_acquisitionmode('Continuous')
        camera.acq_start()
        im = camera.get_nparray()
        camera.acq_stop() 
        
        
        print("Acquired image shape:", im.shape)
        camera.debug = True
        camera.set_exposure(1)
        camera.get_exposure()
        camera.get_rate()
        
        camera.get_stream_mode()
        camera.set_stream_mode()

        
    
        camera.close()