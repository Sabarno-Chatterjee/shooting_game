from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-370, 250)
        self.score = 0
        self.update_scoreboard()
        self.write(f"{self.score}", font=FONT)

    def update_scoreboard(self):
        self.score += 1

# def line():
