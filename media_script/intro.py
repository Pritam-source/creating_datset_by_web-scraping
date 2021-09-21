from manim import *

class DataExtractor(Scene):
   
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        intro=Text("HI!!   I'm  Pritam",font="Noto Sans",color='#5983FC',size=1)
        profile=Text("A Data Extractor",font="Noto Sans",color='#313866',size=1)
        self.play(Write(intro))
        self.wait(1)
        self.remove(intro)
        self.play(Write(profile))
        self.wait(1)
        self.remove(profile)