from turtle import *

pencolor('blue')
pensize(1)
speed('slowest')

for i in range(6):
    fd(100) # forward distance
    lt(360/6) # left turn
    for i in range(6):
         fd(150)
         lt(360/3)

hideturtle()
mainloop()