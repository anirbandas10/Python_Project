#Python program to draw spiral star in turtle programming
import turtle
 
t = turtle.Turtle()
side = 200
for i in range(100):
   t.forward(side)
   t.right(144) #Exterior angle of a star is 144 degree
   side = side - 2

#Python program to draw spiral triangle in turtle programming 
t = turtle.Turtle()
side = 200
for i in range(70):
   t.forward(side)
   t.right(120) #Exterior angle of a triangle is 120 degree
   side = side - 3

#Python program to draw spiral pentagon in turtle programming 
t = turtle.Turtle()
side = 200
for i in range(104):
   t.forward(side)
   t.right(72) #Exterior angle of a pentagon is 72 degree
   side = side - 2

#Python program to draw spider web in turtle programming
t = turtle.Turtle()
t.speed(0)
 
#Code for building radical thread
for i in range(6):
  t.forward(150)
  t.backward(150)
  t.right(60)
 
#Code for building spiral thread
side = 150
for i in range(15):
  t.penup()
  t.goto(0,0)
  t.pendown()
  t.setheading(0)
  t.forward(side)
  t.right(120)
  for j in range(6):
    t.forward(side)
    t.right(60)
  side = side - 10