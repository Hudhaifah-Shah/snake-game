#!/usr/bin/env python3
from turtle import Screen, done
import time
from snake import Snake
from food import Food
from scoreboard import Score
screen = Screen()
screen.setup(width=710, height=710)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
game_on = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(screen.bye, "q")

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.increment_score()
        snake.extend()
    walls_x = snake.head.xcor() > 340 or snake.head.xcor() < -340
    walls_y = snake.head.ycor() > 340 or snake.head.ycor() < -340
    if walls_x or walls_y:
        score.reset()
        snake.reset_snake()

        # game_on = False
        # score.game_over()
    for block in snake.snake[1:]:
        if snake.head.distance(block) < 10:
            score.reset()
            snake.reset_snake()
            # game_on = False
            # score.game_over()
