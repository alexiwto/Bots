import turtle
import time
import random

# Declarations
window = turtle.Screen()
player = turtle.Turtle()
food = turtle.Turtle()
score = turtle.Turtle()
snakebody = []
milisecond = 0.1
actual_score = 0
high_score = 0

# Initialize
def startwindow():
    window.title("Game_001")
    window.bgcolor("#D5B0A8")
    window.setup(600, 600)
    window.tracer(0)


def startplayer():
    player.speed(0)
    player.shape("square")
    player.penup()  # No deja rastro al moverse
    player.goto(0, 0)
    player.direction = "stop"


def spawnfood():
    food.speed(0)
    food.shape("circle")
    food.penup()
    food.color("green")
    food.goto(100, 0)


def startscore():
    score.speed(0)
    score.penup()
    score.hideturtle()
    score.goto(0, 260)
    score.write("Score: 0    High Score: 0", align = "center", font = ("Arial",22, "normal"))

def addbody():
    body = turtle.Turtle()
    body.speed(0)
    body.shape("square")
    body.color("darkgrey")
    body.penup()  # No deja rastro al moverse
    return body


# Controls
def playerup():
    player.direction = "up"


def playerdown():
    player.direction = "down"


def playerright():
    player.direction = "right"


def playerleft():
    player.direction = "left"


def keyboard():
    window.listen()
    window.onkeypress(playerup, "Up")
    window.onkeypress(playerdown, "Down")
    window.onkeypress(playerleft, "Left")
    window.onkeypress(playerright, "Right")


# Collision
def foodcollision():
    if player.distance(food) < 20:
        # newfood
        randx = random.randint(-280, 280)
        randy = random.randint(-280, 280)
        food.goto(randx, randy)
        # addbody
        snakebody.append(addbody())
        #up score
        global actual_score
        global high_score
        actual_score += 1
        if actual_score > high_score:
            high_score = actual_score
        score.clear()
        score.write("Score: {}  High Score: {}".format(actual_score,high_score), align = "center", font = ("Arial", 22, "normal"))

def wallcollision():
    if player.xcor() > 290 or player.xcor() < -290 or player.ycor() > 290 or player.ycor() < -290:
        #Send player back to 0,0
        time.sleep(1)
        player.goto(0, 0)
        player.direction = "stop"
        #Yeet previous body
        for body in snakebody:
            body.goto(1000, 1000)
        snakebody.clear()
        score.clear()
        global actual_score
        global high_score
        actual_score = 0
        score.write("Score: {}  High Score: {}".format(actual_score,high_score), align = "center", font = ("Arial", 22, "normal"))

# Movement()
def bodymovement():
    bodylen = len(snakebody)
    for index in range(bodylen - 1, 0, -1):
        x = snakebody[index - 1].xcor()
        y = snakebody[index - 1].ycor()
        snakebody[index].goto(x, y)

    if bodylen > 0:
        x = player.xcor()
        y = player.ycor()
        snakebody[0].goto(x, y)




def movement():
    if player.direction == "up":
        y = player.ycor()
        player.sety(y + 20)

    if player.direction == "down":
        y = player.ycor()
        player.sety(y - 20)

    if player.direction == "right":
        x = player.xcor()
        player.setx(x + 20)

    if player.direction == "left":
        x = player.xcor()
        player.setx(x - 20)


# Window loop
def updatewindow():
    while True:
        window.update()
        foodcollision()
        bodymovement()
        keyboard()
        movement()
        wallcollision()

        for body in snakebody:
            if body.distance(player) < 20:
                time.sleep(1)
                player.goto(0, 0)
                player.direction = "stop"

                # Yeet the body
                for body in snakebody:
                    body.goto(1000, 1000)
                snakebody.clear()
                actual_score = 0

        time.sleep(milisecond)


# Main program

#Initialize variables
startwindow()
startscore()
startplayer()
spawnfood()

#Infinite Loop
updatewindow()
