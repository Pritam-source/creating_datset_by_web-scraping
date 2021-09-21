from manim import *

class DataExtractor(Scene):
   
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        want=Text("Want details of all Disney movies in one place",font="Noto Sans",color='#5983FC',size=1)
        
        self.play(Write(want))
        self.wait(1)
        self.remove(want)
        