from turtle import Turtle


class Bullet:
    def __init__(self):
        self.all_bullets = []

    def create_bullet(self):
        bullet = Turtle()
        bullet.shape("square")
        bullet.setheading(90)
        bullet.penup()
        bullet.shapesize(stretch_wid=0.2, stretch_len=0.5)
        # self.x_move = 10
        bullet.y_move = 10
        bullet.bullet_speed = 0.1
        self.all_bullets.append(bullet)

    def shoot(self):
        for bullet in self.all_bullets:
            x_position = bullet.xcor()
            y_position = bullet.ycor() + bullet.y_move
            bullet.goto(x_position, y_position)
