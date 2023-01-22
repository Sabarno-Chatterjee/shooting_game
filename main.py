from turtle import Screen
from gun import Gun, Bullet
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.listen()
screen.tracer(0)



gun = Gun()
bullet = Bullet()
screen.onkey(fun=gun.move_right, key="Right")
screen.onkey(fun=gun.move_left, key="Left")
screen.onkey(fun=bullet.shoot, key="space")


is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(1)







screen.exitonclick()