from turtle import Turtle
class OutLine(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-300,250)
    def movement(self):
        self.setheading(0)
        self.pendown()
        self.color("white")
        self.forward(600)