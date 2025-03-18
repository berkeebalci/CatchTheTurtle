import turtle
import random

# Screen setting
screen = turtle.Screen()
screen.title("Catch The Turtle")
screen.bgcolor("lightblue")
screen.setup(width=800, height=600)

# Click the turtle
turtle_obj = turtle.Turtle()
turtle_obj.shape("turtle")
turtle_obj.color("green")
turtle_obj.shapesize(2.2)
turtle_obj.penup()
turtle_obj.speed(0)

# Score
score = 0

# Score Writer
score_table = turtle.Turtle()
score_table.hideturtle()
score_table.penup()
score_table.goto(0, 260)
score_table.color("darkblue")

def score_writer():
    score_table.clear()
    score_table.write(f"Skor: {score}", align="center", font=("Arial", 20, "bold"))

def catch(x, y):
    global score
    score += 1
    score_writer()

def turtle_move():
    x = random.randint(-380, 380)
    y = random.randint(-280, 280)
    turtle_obj.goto(x, y)
    screen.ontimer(turtle_move, 1000)

# Starters
turtle_obj.onclick(catch)
score_writer()
turtle_move()
screen.mainloop()
