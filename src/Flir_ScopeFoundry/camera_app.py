# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 12:33:32 2020

@authors: Alberto Ghezzi, Andrea Bassi. Politecnico di Milano
"""
from ScopeFoundry import BaseMicroscopeApp

class camera_app(BaseMicroscopeApp):
    

    name = 'camera_app'
    
    def setup(self):
        
        #Add hardware components
        print("Adding Hardware Components")
        from camera_hw import FlirHW
        self.add_hardware(FlirHW(self))
           
        # Add measurement components
        print("Create Measurement objects")
        from camera_measure import FlirMeasure
        self.add_measurement(FlirMeasure(self))


if __name__ == '__main__':
    import sys
    
    app = camera_app(sys.argv)
    sys.exit(app.exec_())