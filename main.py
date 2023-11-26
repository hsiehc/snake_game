from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

new_snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_is_on = True
# snake movements
screen.listen()
screen.onkey(new_snake.move_up, 'Up')
screen.onkey(new_snake.move_down, 'Down')
screen.onkey(new_snake.move_left, 'Left')
screen.onkey(new_snake.move_right, 'Right')

while game_is_on:
    screen.update()
    time.sleep(0.1)
    new_snake.move()

    if new_snake.head.distance(food) < 15:
        new_snake.extend()
        food.refresh()
        scoreboard.add_score()

screen.exitonclick()
