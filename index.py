
import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Golden Star")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(1.2)

for i in range(150):
    hue = 0.12 - (i / 150) * 0.12
    t.pencolor(colorsys.hsv_to_rgb(hue, 1, 1))
    t.forward(i * 2.8)
    t.right(165)

turtle.done()
