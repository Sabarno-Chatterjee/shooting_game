from turtle import Screen, Turtle
from gun import Gun
from bullet import Bullet
from raiders import Raiders
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.listen()
screen.tracer(0)

line = Turtle()
line.hideturtle()
line.penup()
line.goto(-400,-200)
line.pendown()
line.pensize(width=2)
line.forward(800)

gun = Gun()
bullet = Bullet()
raider = Raiders()
scoreboard = Scoreboard()
screen.onkey(fun=gun.move_right, key="Right")
screen.onkey(fun=gun.move_left, key="Left")
screen.onkey(fun=bullet.shoot, key="space")


is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()
    raider.create_raider()
    raider.move_raiders()





    for shoot in range(10):
        bullet.shoot()







screen.exitonclick()