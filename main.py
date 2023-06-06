from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)


bet = screen.textinput("Turtle Race Game", "Please choose a turtle (yellow/red/green/blue/purple) to bet on: ")
print(bet)
y_positions = [-120, -60, 0, 60, 120]
color = ["yellow", "red", "green", "blue", "purple"]
all_turtles = []
finish = True

for turtle_index in range(0, 5):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.penup()
    new_turtle.color(color[turtle_index])
    new_turtle.goto(x=-240, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if bet:
    finish = True

while finish:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            finish = False

            winning_turtle = turtle.pencolor()
            if winning_turtle == bet:
                print (f"You won, the {winning_turtle} turtle has won")
            else:
                print(f"You loose, the {winning_turtle} turtle has won")
        running_distance = random.randint(0, 10)
        turtle.forward(running_distance)

screen.bye()

