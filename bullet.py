from turtle import Turtle
from gun import Gun


class Bullet:
    def __init__(self):
        self.all_bullets = []

    def create_bullet(self):
        bullet = Turtle()
        bullet.penup()
        bullet.shape("square")
        bullet.setheading(90)
        bullet.shapesize(stretch_wid=0.2, stretch_len=0.5)
        bullet.y_move = 10
        bullet.bullet_speed = 0.1
        self.all_bullets.append(bullet)

    def shoot(self):
        for bullet in self.all_bullets:
            y_position = bullet.ycor() + bullet.y_move
            bullet.goto(x = bullet.xcor(),y= y_position)

