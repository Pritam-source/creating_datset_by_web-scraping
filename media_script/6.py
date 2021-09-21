from manim import *

class DataExtractor(Scene):
   
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        want=Text("Always get clean and clutter free data in the desired format",font="Noto Sans",color='#5983FC',size=0.5)
        thank=Text("THANK YOU",font="Noto Sans",color='#5983FC',size=1)
        
        self.play(Write(want))
        self.wait(1)
        self.remove(want)
        self.play(Write(thank))
        self.wait(1)
        self.remove(thank)