#!/usr/bin/env python3
from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 12, 'normal')
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.color("white")
        self.speed(0)
        self.ht()
        self.pu()
        self.sety(330)
        with open("data.txt", mode="r") as file:
            self.highscore = int(file.read())
        self.show_score()
    def show_score(self):
        self.clear()
        self.write(arg=f"Score: {self.current_score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)
    def increment_score(self):
        self.current_score += 1
        self.show_score()
    def reset(self):
        if self.current_score > self.highscore:
            self.highscore = self.current_score
        with open("data.txt", mode="w") as file:
            file.write(str(self.highscore))
        self.current_score = 0
        self.show_score()
    # def game_over(self):
    #     self.home()
    #     self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
