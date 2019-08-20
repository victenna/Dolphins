import turtle
import math
import time
wn = turtle.Screen()
wn.bgcolor('green')
wn.setup(1000,800)
wn.bgpic('sea.gif')
turtle.tracer(2)

image=['d1.gif','d7.gif']



t1=turtle.Turtle('turtle')
t1.color('red')
t1.pensize(5)
t1.up()
t1.hideturtle()
t1.goto(-400,-100)
t1.showturtle()
t1.speed(10)
i=-400
while True:
    i=i+1
    if i<=-200 or (i>=0 and i<200):
        wn.addshape(image[0])
        t1.shape(image[0])
    if (i>=-200 and i<0) or (i>=200):
        wn.addshape(image[1])
        t1.shape(image[1])
    
    X=i
    Y=-400+abs(500*math.sin(3.14*i/400))
   
    if X<0:
        t1.setheading(-50*math.cos(3.14*i/400))
    else:
        t1.setheading(50*math.cos(3.14*i/400))
        
    time.sleep(0.0001)
    t1.setposition(X,Y)
    if X>400:
        i=-400
        t1.hideturtle()
        t1.goto(-400,-100)
        t1.showturtle()
    
  
