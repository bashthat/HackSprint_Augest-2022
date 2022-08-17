import turtle
from turtle import Screen
from turtle import *

"""
a graph test for design
"""


colors = ['red', 'blue', 'green', 'yellow', 'purple', 'white']
myTurtle = turtle.Turtle()
for i in range(360):
    myTurtle.pencolor(colors[i % 6])
    myTurtle.width(i / 100 + 1)
    myTurtle.forward(i)
    myTurtle.left(59)
    myTurtle.speed(0)