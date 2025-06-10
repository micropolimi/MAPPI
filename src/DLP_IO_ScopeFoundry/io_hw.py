"""
Code for controlling the DLP Design - Input/Output (IO8G) device.
"""

from ScopeFoundry import HardwareComponent 
from serial import Serial

class IoHW(HardwareComponent):
    """
    Define a new class ShutterHW, defined as a subclass of Hardware component (defined in ScopeFoundry)
    """
    name = 'DLP_IO' 
    
    
    def setup(self):
        """
        The setup function creates the logged quantities we need for controlling the shutter
        """
        #creates a port value in the GUI
        self.port = self.add_logged_quantity('port', dtype=str, initial = 'COM3') 
        #creates a boolean in the GUI for controlling the shutter
        self.channel_1 = self.add_logged_quantity('channel_1', dtype=bool, initial = False) 
        self.ON1 = b'1'
        self.OFF1 = b'Q'
        
    def connect(self):
        self.dlp = Serial(port=self.port.val, baudrate=115200)  
        self.channel_1.hardware_set_func = self.set_channel
        self.channel_1.hardware_read_func = self.is_on
        self.port.change_readonly(True)

    def disconnect(self):
        self.port.change_readonly(False)
        if hasattr(self, 'dlp'):
            self.turn_off()
            self.dlp.close()         # close the port
            del self.dlp
    
    def turn_on(self):
        self.dlp.write(self.ON1)
        self.settings['channel_1'] = True
    
    def turn_off(self):
        self.dlp.write(self.OFF1)
        self.settings['channel_1'] = False
          
    def set_channel(self,state):
        if hasattr(self, 'dlp'):
            if state == True:
                self.turn_on()
            else:
                self.turn_off()
                
    def is_on(self):
        return self.settings.channel_1.val          
        
        
        