#!/usr/bin/env python3
from turtle import Turtle
X = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
    def create_snake(self):
        for i in X:
            self.add_block(i)
    def add_block(self, position):
            block = Turtle("square")
            block.pu()
            block.color("white")
            block.goto(position)
            self.snake.append(block)
    def extend(self):
        self.add_block(self.snake[-1].position())
    def reset_snake(self):
        for block in self.snake:
            block.ht()
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            new_pos = self.snake[i-1].position()
            self.snake[i].goto(new_pos)
        self.head.fd(MOVE_DISTANCE)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
