#Space invaders
# Scoring - calculate score in iscollision


import turtle
import os
import math #needed for collisions
import random # needed to position the enemies in different places


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

# Set the Score to Zero
score = 0
# draw a score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color('white')
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))
score_pen.hideturtle()




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

# choose a number of enemies
number_of_enemies = 5
# Create an empty list of enemies
enemies = []

# Add enemies to the list
for i in range(number_of_enemies):
    # Create the invaders
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color('green')
    enemy.shape('circle')
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

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False


#create Keyboard bindings
turtle.listen()
turtle.onkey(move_left, 'Left')
turtle.onkey(move_right, 'Right')
turtle.onkey(fire_bullet, 'space')


# Main Game Loop
while True:

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
            scorestring ='Score: %s' %score
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





