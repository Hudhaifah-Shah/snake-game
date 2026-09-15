#!/usr/bin/env python3
from turtle import Turtle
from random import randint
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed(0)
        self.refresh()
    def refresh(self):
        random_x = randint(-325, 325)
        random_y = randint(-325, 315)
        self.goto(random_x, random_y)
