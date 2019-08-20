import turtle
import time
wn = turtle.Screen()
wn.setup(1000,800)
wn.tracer(2)
image0=[]
for i in range (15):
    i1=str(i)
    image0.append(i1+'.gif')
image=['do1_2.gif','do2_2.gif']
t1=turtle.Turtle()
wn.addshape(image[0])
t1.shape(image[0])
t1.hideturtle()
t1.up()
t2=turtle.Turtle()
wn.addshape(image[1])
t2.shape(image[1])
t2.hideturtle()
t2.up()
def motion(turtle,angle,n):
    global k
    turtle.setheading(angle)
    turtle.showturtle()
    for i in range(n):
        k=k+1
        k1=k%15
        k2=k%29
        wn.bgpic(image0[k1])
        turtle.fd(40)
        time.sleep(0.03)
    turtle.hideturtle()
while True:
    k=-1
    t1.goto(-300,-200)
    motion(t1,45,10)
    position=t1.position()
    k=-1
    t2.setposition(position)
    motion(t2,-45,20)
    
