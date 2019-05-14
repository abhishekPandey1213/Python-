import turtle

def drawSquare():
    window=turtle.Screen()
    window.bgcolor("red")
    brad=turtle.Turtle()
    brad.shape("circle")
    brad.speed(2)
    brad.color("yellow")
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

def drawcircle():
    window=turtle.Screen()
    window.bgcolor("red")
    angie=turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
def drawtriangle():
    window=turtle.Screen()
    window.bgcolor("red")
    
    t=turtle.Turtle()
    t.forward(200)
    t.left(120)
    t.forward(200)
    t.left(120)
    t.forward(200)
    
    
    window.exitonclick()
drawSquare()
drawcircle()
drawtriangle()
