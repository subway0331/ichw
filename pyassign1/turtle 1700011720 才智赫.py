def sun():
    sun = turtle.Turtle()
    sun.shape("circle")
    sun.shapesize(1.3)
    sun.color("red")
def re(planet,color):
    planet.shape("circle")
    planet.shapesize(0.5)
    planet.color(color)
def updo(planet,x,y):
    planet.up()
    planet.setpos(x,y)
    planet.down()
def elli():
    s=100
    for i in range(s+1):
        ll=2*math.pi/s*i
        for j in range(6):
            p[j].goto(q[j][0]*math.cos(ll),q[j][1]*math.sin(ll))
        
import math
import turtle       
bg=turtle.Screen()
bg.bgcolor("black")
p=[0]
colour=["silver","yellow","green","orange","white","blue"]
q=[[29,27],[54,50],[75,70],[114,110],[390,200],[715,300]]
for i in range(6):
    p.append(i)
    p[i]=turtle.Turtle()
    p[i].speed(0)
    re(p[i],colour[i])
    updo(p[i],q[i][0],0)
sun()
for ring in range(5):
    elli()


