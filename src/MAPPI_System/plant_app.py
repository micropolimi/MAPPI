# -*- coding: utf-8 -*-
"""
Created on Mar 20 12:45:26 2024

@authors: Andrea Bassi. Politecnico di Milano
"""
from ScopeFoundry import BaseMicroscopeApp


def add_path(path):
    import sys
    import os
    # add path to ospath list, assuming that the path is in a sybling folder
    from os.path import dirname
    sys.path.append(os.path.abspath(os.path.join(dirname(dirname(__file__)),path)))


class mappi_app(BaseMicroscopeApp):
    

    name = 'mappi_app'
    
    def setup(self):
        
        #Add hardware components
        print("Adding Hardware Components")
        add_path('Flir_ScopeFoundry')
        from camera_hw import FlirHW
        
        cameray = FlirHW(self, name='camera_y')
        cameray.settings['serial'] = '17289280'
        self.add_hardware(cameray)
        
        camerax = FlirHW(self, name='camera_x')
        camerax.settings['serial'] = '14103019'
        self.add_hardware(camerax)
        
        add_path('DLP_IO_ScopeFoundry')
        from io_hw import IoHW
        self.add_hardware(IoHW(self, name='led_y'))
        self.add_hardware(IoHW(self, name='led_x'))
         
        # Add measurement components
        print("Create Measurement objects")

        from plant_timelapse_dual_measure import PlantTimeLapseDualMeasure
        self.add_measurement(PlantTimeLapseDualMeasure(self))


if __name__ == '__main__':
    import sys
    import os

    app = mappi_app(sys.argv)
    
    path = os.path.dirname(os.path.realpath(__file__))
    new_path = os.path.join(path, 'Settings', 'newsettings.ini')

    app.settings_load_ini(new_path)



    for hc_name, hc in app.hardware.items():
          hc.settings['connected'] = True    # connect all the hardwares  
    
    sys.exit(app.exec_())