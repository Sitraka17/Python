from turtle import *

color('black', 'magenta')

def left_turn(length):
    for i in range(10):
        forward(length/10)
        left(9)
        
def petal(size):
    begin_fill()
    left_turn(size)
    left(90)
    left_turn(size)
    left(90)
    end_fill()

# Loop through the "petal spiral" 
for i in range(0, 200, 10):
    petal(i) # Petal takes an input for size
    right(360/10)
    
bye()
