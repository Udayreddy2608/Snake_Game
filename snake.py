from turtle import Screen
from snake_classes import Snake
from food import Food
from scoreboard import ScoreBoard
from outline import OutLine
import time


screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score=ScoreBoard()
outline=OutLine()

screen.listen()
screen.onkey(key="Up" , fun=snake.up)
screen.onkey(key="Down" , fun=snake.down)
screen.onkey(key="Left" , fun=snake.left)
screen.onkey(key="Right" , fun=snake.right)
game_on = True


while game_on:
    screen.update()
    time.sleep(0.1)
    outline.movement()
    snake.move()
    if snake.head.distance(food)<15:
        score.score+=1
        snake.extend()
        score.clear()
        score.refresh()
        food.refresh()
    #DETECT COLLISION
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>240 or snake.head.ycor()<-280:
        game_on=False
    for segments in snake.snakes:
        if segments==snake.head:
            pass
        elif snake.head.distance(segments)<10:
            game_on=False


score.game_over()
screen.exitonclick()