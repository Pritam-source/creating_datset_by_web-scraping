from manim import *

class DataExtractor(Scene):
   
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        want=Text("Got cluttered data ! \n   NO PROBLEM\n Let's clean the data",font="Noto Sans",color='#5983FC',size=1,line_spacing=1)
        
        self.play(Write(want))
        self.wait(1)
        self.remove(want)