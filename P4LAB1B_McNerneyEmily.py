#CTI-110
#P4HW2 - Initials
#Emily McNerney
#April 24, 2023
#

import turtle

t = turtle.Turtle()
t.penup()
# draw straight line
t.goto(-150, 50)
t.pendown()
t.pensize(10)
t.pencolor("blue")

t.forward(100)
t.backward(100)

t.right(90)
t.forward(75)

t.left(90)
t.forward(100)
t.backward(100)
t.right(90)

t.forward(75)
t.left(90)
t.forward(100)

t = turtle.Turtle()
t.penup()
# draw straight line
t.goto(-30, 50)  # centering in the screen
t.pendown()
t.pensize(10)
t.pencolor("blue")

t.right(90)
t.forward(150)

t.goto(-30, 50)
t.goto(20, -20)
t.goto(65, 50)
t.goto(65, -100)


# Keep the window open until it is closed by the user
turtle.done()