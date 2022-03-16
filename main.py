import turtle
from turtle import Turtle, Screen
import random


screen = Screen()
is_race_on = False
screen.setup(width=400, height=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []


yy = -100

for x in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[x])
    new_turtle.penup()
    new_turtle.goto(x=-180, y=yy)
    all_turtles.append(new_turtle)
    yy +=30

if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 165:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_dist = random.randint(0, 10)
        turtle.forward(random_dist)



screen.exitonclick()
