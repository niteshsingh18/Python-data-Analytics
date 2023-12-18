from turtle import *

s = Screen()
s.setup(1000,1000)

bgcolor('black')
speed('fastest')
colors = ['red', 'purple', 'yellow', 'blue', 'green', 'orange']
for x in range(360):
    pencolor(colors[x % 6])
    width(x / 100 + 1)
    forward(x)
    left(59)

hideturtle()
mainloop()

