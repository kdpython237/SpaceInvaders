# Space invaders
# Add RMusic

import turtle
import os
import math  # needed for collisions
import random  # needed to position the enemies in different places
import winsound  # required for sound for game
import platform  # sounds for all platforms

#if on windows you need to import winsound or better yet just use linux
if platform.system() == 'Windows':
    try:
        import winsound
    except:
        print('Winsound module not avialable')

# Setup the screen
# Create a screen window lets use wn
wn = turtle.Screen()
wn.bgcolor('Blue')
wn.title('Space Invaders')
# This adds a stary background
wn.bgpic('background.gif')
wn.tracer(0)


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
player.speed(0)  # this is the speed the shape is drawn at this calls the method
player.setposition(0, -250)
player.setheading(90)  # this calls the variable

# Make the Defender move
# set a speed for you player
player.speed = 0

# choose a number of enemies
number_of_enemies = 50
# Create an empty list of enemies
enemies = []

# Add enemies to the list
for i in range(number_of_enemies):
    # Create the invaders
    enemies.append(turtle.Turtle())

enemy_start_x = -225
enemy_start_y = 250
enemy_number = 0

for enemy in enemies:
    enemy.color('green')
    enemy.shape('invader2.gif')
    enemy.penup()
    enemy.speed(0)
    x = enemy_start_x + (50 * enemy_number)
    y = enemy_start_y
    enemy.setposition(x, y)
    # Update the enemy number
    enemy_number += 1
    if enemy_number == 10:
        enemy_start_y -= 50
        enemy_number = 0

enemyspeed = 0.1

# Create a weapon for our player
bullet = turtle.Turtle()
bullet.color('red')
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 5

# fire bullet is on its way to target
bulletstate = 'ready'

# Function move player left
def move_left():
    player.speed = -1

# Function move player right
def move_right():
    player.speed = 1


def move_player():
    x = player.xcor()
    x += player.speed
    if x < -280:
        x = -280
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    # declare bulletstate as a global
    global bulletstate
    if bulletstate == 'ready':
        play_sound("shoot.wav")
        bulletstate = 'fire'
        # move the bullet to just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2)+math.pow(t1.ycor()-t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False

def play_sound(sound_file, time = 0):
    # Windows
    if platform.system() == 'Windows':
        winsound.PlaySound(sound_file, winsound.SND_ASYNC)
    # Linux
    elif platform.system() == 'Linux':
        os.system('aplay -q {}&'.format(sound_file))
    # MAC
    else:
        os.system('afplay {}&'.format(sound_file))

    # Repeat Sound
    if time > 0:
        turtle.ontimer(lambda: play_sound(sound_file, time), t=int(time * 1))


# create Keyboard bindings
wn.listen()
wn.onkeypress(move_left, 'Left')
wn.onkeypress(move_right, 'Right')
wn.onkeypress(fire_bullet, 'space')

# Play Background Music
# play_sound('R2F.wav', 112)

# Main Game Loop
while True:

    wn.update()
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
            play_sound("invaderkilled.wav")
            #reset bullet
            bullet.hideturtle()
            bulletstate='ready'
            bullet.setposition(0, -400)
            #reset enemy
            enemy.setposition(0, 15000)

            #Update Score
            score +=10
            scorestring ="Score: {}" .format(score)
            score_pen.clear()
            score_pen.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))

        if isCollision(player, enemy):
            playsound("explosion.wav")
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




