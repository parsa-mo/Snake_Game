import time
from turtle import Screen
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

sam = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(sam.left, 'Left')
screen.onkey(sam.right, 'Right')
screen.onkey(sam.up, 'Up')
screen.onkey(sam.down, 'Down')
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    sam.move()

    # Detect collision with food
    if sam.head.distance(food) < 20:
        food.refresh()
        scoreboard.refresh()
        sam.extend()

    # Detect collision with wall
    if sam.head.xcor() > 290 or sam.head.xcor() < -290 or sam.head.ycor() > 290 or sam.head.ycor() < -290:
        scoreboard.game_over()
        game_on = False

    # Detect collision with tail
    for segment in sam.snake[1:]:
        if sam.head.distance(segment) < 10:
            scoreboard.game_over()
            game_on = False


screen.exitonclick()
