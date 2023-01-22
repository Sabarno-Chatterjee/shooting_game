from turtle import Turtle


class Gun(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.setheading(90)
        self.shapesize(stretch_wid=3, stretch_len=1.5)
        self.penup()
        self.goto((0, -280))
        self.move_left()
        self.move_right()

    def move_right(self):
        x_position = self.xcor() + 20
        self.goto(x_position, y=self.ycor())

    def move_left(self):
        x_position = self.xcor() - 20
        self.goto(x_position, y=self.ycor())


class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.2)

    def shoot(self):
        if self.xcor() < 300:
            self.forward(20)
