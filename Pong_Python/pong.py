# Pong using turtle
# Adapted from TokyoEdTech

import turtle
import random
import numpy
import math

window = turtle.Screen() # create the window for the game
window.title("Pong")
window.bgcolor("#54494B")
window.setup(width=800,height=600)
window.tracer(0) # stops the window from updating

# Decoration
seperator = turtle.Turtle()
seperator.shape("square")
seperator.shapesize(stretch_wid= 40, stretch_len= 0.2)
seperator.color("#B33951")

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # the speed of animation
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("#91C7B1")
paddle_a.penup()
paddle_a.goto(-350, 0) # initial coordination

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) # the speed of animation
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("#91C7B1")
paddle_b.penup()
paddle_b.goto(350, 0) # initial coordination

# Ball
ball = turtle.Turtle()
ball.speed(0) # the speed of animation
ball.shape("circle")
ball.color("#E3D081")
ball.penup()
ball.goto(0, 0) # initial coordination
delta_speed = 1
ball.dx = delta_speed
ball.dy = delta_speed

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("#F1F7ED")
pen.penup()
pen.hideturtle()
pen.goto(0,240)
pen.write("0  0", align="center", font=("Courier", 30, "bold"))

# Functions
def paddle_a_up():
    y = paddle_a.ycor() # y coodinate of paddle a
    if y < 250:
        y += 20
        paddle_a.sety(y) # set y coordinate to the new y
    else:
        paddle_a.sety(250)

def paddle_a_down():
    y = paddle_a.ycor() # y coodinate of paddle a
    if y > -250: 
        y -= 20
        paddle_a.sety(y) # set y coordinate to the new y
    else:
        paddle_a.sety(-250)

def paddle_b_up():
    y = paddle_b.ycor() # y coodinate of paddle b
    if y < 250:
        y += 20
        paddle_b.sety(y) # set y coordinate to the new y
    else:
        paddle_b.sety(250)

def paddle_b_down():
    y = paddle_b.ycor() # y coodinate of paddle b
    if y > -250: 
        y -= 20
        paddle_b.sety(y) # set y coordinate to the new y
    else:
        paddle_b.sety(-250)
    
# Keyboard binding
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

# Main funtion
while True:
    window.update() # everytime the loop runs, the window updates

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.goto(0,0)
        offset = random.randrange(9,16)
        ball.dx = random.choice([-1,1]) * numpy.sin(4*math.pi/offset)
        ball.dy = -1 * numpy.cos(4*math.pi/offset)
        score_a += 1
        pen.clear() # clear the previous score 
        pen.write(f"{score_a}  {score_b}", align="center", font=("Courier", 30, "bold"))
    elif ball.xcor() < -390:
        ball.goto(0,0)
        offset = random.randrange(9,16)
        ball.dx = random.choice([-1,1]) * numpy.sin(4*math.pi/offset)
        ball.dy = numpy.cos(4*math.pi/offset)
        score_b += 1
        pen.clear() # clear the previous score 
        pen.write(f"{score_a}  {score_b}", align="center", font=("Courier", 30, "bold"))

    # Paddle and ball collisions
    # Paddle B and ball
    if (ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40) and (ball.ycor() > paddle_b.ycor() - 40):
        ball.dx *= -1 
    # Paddle A and ball
    elif (ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40) and (ball.ycor() > paddle_a.ycor() - 40):
        ball.dx *= -1 

