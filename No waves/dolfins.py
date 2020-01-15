import turtle
import time
wn = turtle.Screen()
wn.setup(800,800)
wn.tracer(2)
wn.bgpic('more.gif')

image=['do1.gif','do2.gif']
wn.addshape(image[0])
wn.addshape(image[1])
t1=turtle.Turtle()
t1.up()
while True:
    t1.shape(image[0])
    t1.goto(-300,-300)
    t1.setheading(45)
    for i in range(30):
        t1.shape(image[0])
        t1.fd(20)
        time.sleep(0.05)
    t1.setheading(-45)
    for i in range(30):
        t1.shape(image[1])
        t1.fd(20)
        time.sleep(0.05)
    time.sleep(0.5)
