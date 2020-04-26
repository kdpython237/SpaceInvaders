#Space invaders

import turtle
import os

#setup the screen
#Create a screen window lets use wn
wn = turtle.Screen()
wn.bgcolor("Black")
wn.title("Space Invaders")

# Draw a Border for the game
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Create the Player turtle
player = turtle.Turtle()
player. color('green')
player.shape('triangle')
player.penup()
player.speed(0) #this is the speed the sahpe is drawn at
player.setposition(0, -250)
player.setheading(90)



