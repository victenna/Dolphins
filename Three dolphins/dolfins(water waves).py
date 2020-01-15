import turtle
import time
wn = turtle.Screen()
wn.setup(1000,800)
turtle.tracer(3)

image0=[]
for i in range (15):
    i1=str(i)
    image0.append(i1+'.gif')
   
image=['do1.gif','do2.gif']

t1=turtle.Turtle()
t1.up()
k=-1
def motion (direction,img):
    global k
    t1.setheading(direction)
    for i in range(10):
        k=k+1
        k1=k%15
        wn.bgpic(image0[k1])
        wn.addshape(img)
        t1.shape(img)
        t1.fd(40)
        time.sleep(0.05)
while True:
    k=k+1
    k1=k%15
    wn.bgpic(image0[k1])
    t1.goto(-300,-200)
    motion(45,image[0])
    motion(-45,image[1])
    
        
    
    
