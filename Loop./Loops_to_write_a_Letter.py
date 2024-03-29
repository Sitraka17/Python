from turtle import *
width(5)

left(180)

# Start of for loop.
for i in range(5): # Code below is repeated 5 times
    # Code to be repeated 
    forward(50) # Indentation indcates code is inside the loop
    left(45) # Still inside the for loop
# No more indentation! Marks the end of the for-loop.
hideturtle()
bye()


#You can write the C letter in 5 lines rather than this type: 
forward(100)
left(45)
forward(100)
left(45)
forward(100)
left(45)
forward(100)
left(45)
forward(100)
left(45)
#This is longer, it can hardly be improved. 

#A couple of important notes on for loops:
###The number that we put inside range() in the line for i in range(5) is what determines the number of times the loop will repeat. (The range function is covered in a later lesson.)
###Only the code that's indented below the for loop will be repeated (or “looped” over).
###Code inside the for loop needs to be indented in a consistent way.
###The end of the indentation marks the end of the for loop.
