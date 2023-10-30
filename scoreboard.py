from turtle import Turtle
ALIGNMENT="center"
FONT=("Courier",24,"normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("White")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align=ALIGNMENT,font=FONT)
        self.hideturtle()
    def refresh(self):
        self.color("White")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!!!",align="Center",font=("Courier",48,"normal"))



