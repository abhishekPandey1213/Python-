#!/usr/bin/env python3
'''A Python Program to draw shapes using turtle module of python.
In this program we are drawing square ,circle and traingle'''

import turtle



def drawSquare(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)
def drawTriangle(some):
    for i in range(1,3):
        some.forward(50)
        some.left(120)
    some.forward(50)
    

def drawart():
    
    window= turtle.Screen()
    window.bgcolor("red")
    #creat turtle brad
    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
##    for i in range(1,37):
##        
##        drawSquare(brad)
##        brad.right(10)

   
###draw circle angie
##   # angie=turtle.Turtle()
##   # angie.shape("arrow")
##    angie.color("blue")
##    angie.circle(100)
###draw traingle    
    t=turtle.Turtle()
    t.shape("turtle")
    t.color("green")
    for i in range(1,37):
        
        drawTriangle(t)
        t.right(10)
    t.left(90)
    t.forward(200)
    
    
    window.exitonclick()


drawart()
