from turtle import Turtle

class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.setheading(90)
        self.penup()
        self.shapesize(stretch_wid=0.2, stretch_len=0.5)

    def shoot(self):
        if self.xcor() < 300:
            self.forward(20)