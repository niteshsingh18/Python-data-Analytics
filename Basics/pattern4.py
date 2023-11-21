from turtle import *
from random import randint, choice

squares = 0

speed('fastest')
while squares < 100:
    x = randint(-300, 300)
    y = randint(-300, 300)
    size = randint(50, 100)
    penup()
    goto(x,y)
    pendown()
    color = ['red', 'blue', 'purple', 'pink']
    fillcolor(choice(color))
    begin_fill()

    for i in range(4):
        fd(size)
        rt(90)
        circle(size/7)
        rt(360/12)
    end_fill()
    squares += 1

hideturtle()
mainloop()
