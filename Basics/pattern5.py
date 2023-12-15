from turtle import *

title('Meer Magic')
bgcolor('black')
pencolor('white')
pensize(4)

fillcolor('dark blue')
begin_fill()
for i in range(5):
    fd(100)
    lt(72)
end_fill()

fillcolor('sky blue')
begin_fill()
circle(50)
end_fill()

hideturtle()
mainloop()

