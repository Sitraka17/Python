from turtle import *

width(2)

def circle(size):
    penup()
    forward(200)
    pendown()
    left(90)
    for i in range(60):
        forward(size)
        left(6)
    right(90)
    penup()
    back(200)
    pendown()

circle(10)
circle(20)

bye()
