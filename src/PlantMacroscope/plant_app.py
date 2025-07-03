# -*- coding: utf-8 -*-
"""
Created on Mar 20 12:45:26 2024

@authors: Andrea Bassi. Politecnico di Milano
"""
from ScopeFoundry import BaseMicroscopeApp

class camera_app(BaseMicroscopeApp):
    

    name = 'plant_app'
    
    def setup(self):
        
        #Add hardware components
        print("Adding Hardware Components")
        from camera_hw import FlirHW
        
        cameray = FlirHW(self, name='camera_y')
        cameray.settings['serial'] = '17289280'
        self.add_hardware(cameray)
        
        camerax = FlirHW(self, name='camera_x')
        camerax.settings['serial'] = '14103019'
        self.add_hardware(camerax)
        
        from io_hw import IoHW
        self.add_hardware(IoHW(self, name='led_y'))
        self.add_hardware(IoHW(self, name='led_x'))
         
        # Add measurement components
        print("Create Measurement objects")

        from plant_timelapse_dual_measure import PlantTimeLapseDualMeasure
        self.add_measurement(PlantTimeLapseDualMeasure(self))

        self.ui.show()
        self.ui.activateWindow()


if __name__ == '__main__':
    import sys

    app = camera_app(sys.argv)
    app.settings_load_ini(".\\Settings\\settings_timelapse_dualview.ini")
    
    for hc_name, hc in app.hardware.items():
          hc.settings['connected'] = True    # connect all the hardwares  
    
    sys.exit(app.exec_())