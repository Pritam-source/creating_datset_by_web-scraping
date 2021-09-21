from manim import *

class DataExtractor(Scene):
   
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        want=Text("Looks Fine , Let's create Data set",font="Noto Sans",color='#5983FC',size=1)
        
        self.play(Write(want))
        self.wait(1)
        self.remove(want)
        