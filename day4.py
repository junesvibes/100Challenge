import turtle

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(5)

for i in range(6):
    for colors in ["Red","purple", "blue", "green", "yellow", "white"]:
        turtle.color(colors)
        turtle.circle (100)
        turtle.left(10)

turtle.hideturtle()