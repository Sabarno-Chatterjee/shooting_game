from turtle import Screen
from gun import Gun

screen = Screen()
screen.setup(width=800, height=600)
screen.listen()



gun = Gun()

screen.onkey(fun=gun.move_right, key="Right")
screen.onkey(fun=gun.move_left, key="Left")











screen.exitonclick()