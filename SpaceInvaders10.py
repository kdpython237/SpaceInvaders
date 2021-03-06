#Space invaders
# Move the bullet

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

# Create the Defending Player turtle
player = turtle.Turtle()
player. color('green')
player.shape('triangle')
player.penup()
player.speed(0) #this is the speed the sahpe is drawn at
player.setposition(0, -250)
player.setheading(90)

# Make the Defender move
# set a speed for you player

playerspeed =15

# Create the invaders
enemy = turtle.Turtle()
enemy.color('green')
enemy.shape('circle')
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)



enemyspeed =2

# Create a weapon for our player
bullet = turtle.Turtle()
bullet.color('red')
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

# define bullet state

# ready to fire

# fire bullet is on its way to target
bulletstate = 'ready'



# Function move player left
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

# Function move player right
def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)


def fire_bullet():
    #declare bulletstate as a global
    global bulletstate
    if bulletstate == 'ready':
        bulletstate = 'fire'
        #move the bullet to just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()






#create Keyboard bindings
turtle.listen()
turtle.onkey(move_left, 'Left')
turtle.onkey(move_right, 'Right')
turtle.onkey(fire_bullet, 'space')


# Main Game Loop
while True:
    #Move the enemy
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)

    # Move the enemy back and down
    if enemy.xcor() > 280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)


    if enemy.xcor() < -280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)

    # move the Bullet
    if bulletstate == 'fire':
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #Check to see if the bullet has gone off the screen
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate='ready'




