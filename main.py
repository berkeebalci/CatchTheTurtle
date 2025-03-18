import turtle
import random
from sys import thread_info

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

# Score , timer and  record
timer = 5
score = 0
record = 0

#Timer Writer
timer_writer = turtle.Turtle()
timer_writer.hideturtle()
timer_writer.penup()
timer_writer.goto(300,260)
timer_writer.color("Red")

# Score Writer
score_table = turtle.Turtle()
score_table.hideturtle()
score_table.penup()
score_table.goto(0, 260)
score_table.color("darkblue")

def time():
    timer_writer.clear()
    timer_writer.write(f"Time: {timer}",align="center",font=("Arial", 16, "bold"))

def game_over():
    turtle_obj.hideturtle()
    score_table.goto(0 , 0)
    score_table.write("GAME OVER!", align="center",font=("Arial",24,"bold"))

def count_down():
    global timer
    if timer > 0:
        timer -= 1
        time()
        screen.ontimer(count_down,1000)
    else:
        game_over()


def score_writer():
    score_table.clear()
    score_table.write(f"Skor: {score} | Record:{record}", align="center", font=("Arial", 20, "bold"))

def catch(x, y):
    global score , record
    score += 1
    if score > record:
        record = score
    score_writer()

def turtle_move():
    x = random.randint(-380, 380)
    y = random.randint(-280, 280)
    turtle_obj.goto(x, y)
    screen.ontimer(turtle_move, 1000)





# Starters
turtle_obj.onclick(catch)
score_writer()
time()
count_down()
turtle_move()
screen.mainloop()
