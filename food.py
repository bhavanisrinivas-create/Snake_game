from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('red')
        self.refresh()
    def refresh(self):
        x=random.randint(-280,280)
        y=random.randint(-280,280)
        self.setpos(x,y)
        