"""
Code written by Michele Castriotta and Andrea Bassi for controlling the Polimi shutter,
sending HIGH and LOW signal to the RTS line of the USB port. The shutter is implemented 
for working in ScopeFoundry (http://www.scopefoundry.org/).

11-10-2018, Milan

This script setup the ScopeFoundry applications, and try the shutter. 
Run it if you want to try the shutter, otherwise is useless.
"""

from ScopeFoundry import BaseMicroscopeApp

class Try_DLP_IO(BaseMicroscopeApp):

    # this is the name of the microscope that ScopeFoundry uses 
    # when storing data
    name = 'try_dlp_io'
    
    # You must define a setup function that adds all the 
    #capablities of the microscope and sets default settings
    def setup(self):
        
        #Add App wide settings
        
        #Add hardware components
        from io_hw import IoHW
        self.add_hardware(IoHW(self))
               
        
        self.ui.show()
        self.ui.activateWindow()


if __name__ == '__main__':
    
    import sys
    app = Try_DLP_IO(sys.argv)
    sys.exit(app.exec_())