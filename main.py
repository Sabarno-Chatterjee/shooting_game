from turtle import Screen
from gun import Gun
from bullet import Bullet
from raiders import Raiders
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.listen()
screen.tracer(0)



gun = Gun()
bullet = Bullet()
raider = Raiders()
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