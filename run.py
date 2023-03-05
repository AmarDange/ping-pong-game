# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import turtle as t
playerAscore=0
playerBscore=0

window=t.screen
window.title("Pong Game")
window.bgcolor("green")
window.setup(width=800,height=600)
window.tracer(0)

#creating left paddle
leftpaddle.t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5,strech_len=1)
leftpaddle.penup()
leftpaddle.goto(-350,0)


#creating right.paddle
rightpaddle.t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5,strech_len=1)
rightpaddle.penup()
rightpaddle.goto(350,0)



#creating ball
ball=t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(5,5)
ballxdirection=0.2
ballydirection=0.2


#creating pen for scorecard update
pen=t.Turtle()
pen.speed(0)
pen.color("Blue")
pen.penup()
pen.hideturtle()
pen.goto(0.260)
pen.write("score",align="center",font=("Arial",24,"normal"))


#moving the leftpaddle

def leftpaddleup():
    y=leftpaddle.ycor()
    y=y+90
    leftpaddle.sety(y)

def leftpaddledown():
    y=leftpaddle.ycor()
    y=y-90
    leftpaddle.sety(y)

#moving the rightpaddle

def rightpaddleup():
    y=rightpaddle.ycor()
    y=y+90
    rightpaddle.sety(y)

def rightpaddledown():
    y=rightpaddle.ycor()
    y=y-90
    rightpaddle.sety(y)