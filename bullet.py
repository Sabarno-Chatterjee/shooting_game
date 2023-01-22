from turtle import Turtle

class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.setheading(90)
        self.penup()
        self.shapesize(stretch_wid=0.2, stretch_len=0.5)
        # self.x_move = 10
        self.y_move = 10
        self.bullet_speed = 0.1

    def shoot(self):
        x_position = self.xcor()
        y_position = self.ycor() + self.y_move
        self.goto(x_position,y_position)