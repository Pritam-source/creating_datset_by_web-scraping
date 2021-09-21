from manim import *

class DataExtractor(Scene):
   
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        want=Text("Not enough information on single website!\n Let's try linked website for more details",font="Noto Sans",color='#5983FC',size=1,line_spacing=1)
        
        self.play(Write(want))
        self.wait(1)
        self.remove(want)
        