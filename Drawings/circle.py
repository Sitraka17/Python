from turtle import *

width(2)

def circle():
    penup()
    forward(50)
    pendown()
    left(90)
    for i in range(60):
        forward(5)
        left(6)
    right(90)
    penup()
    back(50)
    pendown()
    

circle()

bye()

