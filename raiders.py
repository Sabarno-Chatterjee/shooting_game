from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Raiders():

    def __init__(self):
        self.all_raiders = []

    def create_raider(self):
        if random.randint(1, 8) == 1:
            raider = Turtle(shape="square")
            raider.color(random.choice(COLORS))
            raider.shapesize(stretch_len=1, stretch_wid=2)
            raider.penup()
            x_position = random.randint(-380, 380)
            raider.goto(x_position, 310)
            raider.setheading(270)
            self.all_raiders.append(raider)

    def move_raiders(self):
        for raider in self.all_raiders:
            raider.forward(10)
