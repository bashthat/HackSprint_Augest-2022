import turtle
from turtle import *

"""
a graph test for design
"""


colors = ['red', 'blue', 'green', 'yellow', 'purple', 'white']
t = turtle.Turtle()
turtle.bgcolor('black')
for i in range(360):
    t.pencolor(colors[i % 6])
    t.width(i / 100 + 1)
    t.forward(i)
    t.left(59)
    t.speed(0)