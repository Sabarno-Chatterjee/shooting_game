from turtle import Turtle

class Gun(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=0.5)
        self.penup()
        self.goto((0,-280))
        self.move_left()
        self.move_right()

    def move_right(self):
        self.forward(20)

    def move_left(self):
        self.backward(20)
