import random
import turtle

#Screen
screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtle Python")
screen.setup(width=800 , height=600)

#Create Turtle
turtle_obj = turtle.Turtle()
turtle_obj.shape("turtle")
turtle_obj.color("green")
turtle_obj.shapesize(2.2)
turtle_obj.penup()
turtle_obj.speed(0)

screen.tracer(0)

def turtle_random_move():
    x = random.randint(-280,280)
    y = random.randint(-280,280)
    turtle_obj.goto(x,y)
    screen.update()
    screen.ontimer(turtle_random_move,1000)
turtle_random_move()















screen.mainloop()