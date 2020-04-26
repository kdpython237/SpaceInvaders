# Space invaders
# change turtle to wn and got Better Movement

import turtle
import os
import math # needed for collisions
import random # needed to position the enemies in different places
import winsound # required for sound for game

#setup the screen
#Create a screen window lets use wn
wn = turtle.Screen()
wn.bgcolor('Blue')
wn.title('Space Invaders')
# This adds a stary background
wn.bgpic('background.gif')

# register the shapes for our player and enemies
wn.register_shape('invader2.gif')
wn.register_shape('player.gif')


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

# Set the Score to Zero
score = 0
# draw a score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color('white')
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: {}" .format(score)
score_pen.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))
score_pen.hideturtle()

# Create the Defending Player turtle
player = turtle.Turtle()
player. color('green')
player.shape('player.gif')
player.penup()
player.speed(0) #this is the speed the sahpe is drawn at
player.setposition(0, -250)
player.setheading(90)

# Make the Defender move
# set a speed for you player
player.speed = 0

# choose a number of enemies
number_of_enemies = 10
# Create an empty list of enemies
enemies = []

# Add enemies to the list
for i in range(number_of_enemies):
    # Create the invaders
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color('green')
    enemy.shape('invader2.gif')
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

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

# fire bullet is on its way to target
bulletstate = 'ready'

# Function move player left
def move_left():
    player.speed = -15

# Function move player right
def move_right():
    player.speed = 15


def move_player():
    x = player.xcor()
    x += player.speed
    if x < -280:
        x = -280
    if x > 280:
        x = 280
    player.setx(x)



def fire_bullet():
    #declare bulletstate as a global
    global bulletstate
    if bulletstate == 'ready':
        winsound.PlaySound("shoot.wav", winsound.SND_ASYNC)
        bulletstate = 'fire'
        #move the bullet to just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False


#create Keyboard bindings
wn.listen()
wn.onkeypress(move_left, 'Left')
wn.onkeypress(move_right, 'Right')
wn.onkeypress(fire_bullet, 'space')


# Main Game Loop
while True:
    move_player()

    for enemy in enemies:
        #Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        # Move the enemy back and down
        if enemy.xcor() > 280:
            #Move all of the enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Change enemy direction
            enemyspeed *= -1


        if enemy.xcor() < -280:
            for e in enemies:
                #Move all of the enemies down
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Change enemy direction
            enemyspeed *= -1

    #check for collision between bullet and enemy
        if isCollision(bullet, enemy):
            winsound.PlaySound("invaderkilled.wav", winsound.SND_ASYNC)
            #reset bullet
            bullet.hideturtle()
            bulletstate='ready'
            bullet.setposition(0, -400)
            #reset enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            #Update Score
            score +=10
            scorestring ="Score: {}" .format(score)
            score_pen.clear()
            score_pen.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))

        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print('GAME OVER')
            break

    # move the Bullet
    if bulletstate == 'fire':
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #Check to see if the bullet has gone off the screen
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate='ready'






