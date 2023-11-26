from turtle import Turtle
import random

FONT = ("Arial", 20, "normal")

CENTER = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0, 270)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align=CENTER, font=FONT)

    def add_score(self):
        self.score += 1
        self.write_score()
