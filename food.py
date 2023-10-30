from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("red")
        self.shapesize(0.5,0.5)
        r_x=random.randint(-280,280)
        r_y=random.randint(-260,250)
        self.goto(r_x,r_y)
    def refresh(self):
        r_x = random.randint(-280, 280)
        r_y = random.randint(-260, 250)
        self.goto(r_x, r_y)




