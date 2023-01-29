from turtle import *

width(2)

def circle(size):
    penup()
    forward(size*30/3.14) # Updated line
    pendown()
    left(90)
    for i in range(60):
        forward(size)
        left(6)
    right(90)
    penup()
    back(size*30/3.14) # Updated line
    pendown()

# Drawing centered circles 
circle(10)
circle(20)

bye()
