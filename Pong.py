import turtle

#create window
screen = turtle.Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=1000,height=600)
screen.tracer(0)

#Score
scoreL = 0
scoreR = 0

#Paddle L
paddleL = turtle.Turtle()
paddleL.speed(0)
paddleL.shape("square")
paddleL.color("white")
paddleL.shapesize(stretch_wid=5, stretch_len=1)
paddleL.penup()
paddleL.goto(-450,0)

#Paddle R
paddleR = turtle.Turtle()
paddleR.speed(0)
paddleR.shape("square")
paddleR.color("white")
paddleR.shapesize(stretch_wid=5, stretch_len=1)
paddleR.penup()
paddleR.goto(450,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = .2
ball.dy = .2

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("0    0",align="center",font=("Courier",24,"normal"))


#Functions
#Move left paddle
def paddleLUp():
    paddleL.sety((paddleL.ycor())+40)
def paddleLDown():
    paddleL.sety((paddleL.ycor())-40)

#Move right paddle
def paddleRUp():
    paddleR.sety((paddleR.ycor())+40)
def paddleRDown():
    paddleR.sety((paddleR.ycor())-40)

#Keybinds
screen.listen()
screen.onkeypress(paddleLUp, "w")
screen.onkeypress(paddleLDown, "s")
screen.onkeypress(paddleRUp, "Up")
screen.onkeypress(paddleRDown, "Down")

#game loop
while True:
    screen.update()

    #Check if left player wins
    if scoreL >= 5:
        pen.clear()
        pen.write("Player 1 wins!",align="center",font=("Courier",24,"normal"))
        ball.goto(0,0)
        ball.dx=0
        ball.dy=0
    
    #check if right player wins
    if scoreR >= 5:
        pen.clear()
        pen.write("Player 2 wins!",align="center",font=("Courier",24,"normal"))
        ball.goto(0,0)
        ball.dx=0
        ball.dy=0

    #Ball movement
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #Border check
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor()>490:
        ball.goto(0,0)
        ball.dx *= -1
        scoreL += 1
        pen.clear()
        pen.write("{}    {}".format(scoreL,scoreR),align="center",font=("Courier",24,"normal"))
    if ball.xcor()<-490:
        ball.goto(0,0)
        ball.dx *= -1
        scoreR += 1
        pen.clear()
        pen.write("{}    {}".format(scoreL,scoreR),align="center",font=("Courier",24,"normal"))
    
    #Right paddle collision
    if ball.xcor()>440 and ball.xcor()<450 and (ball.ycor()<paddleR.ycor()+50 and ball.ycor()>paddleR.ycor()-50):
        ball.dx *= -1
        ball.setx(440)
    
    #Left paddle collision
    if ball.xcor()<-440 and ball.xcor()>-450 and (ball.ycor()<paddleL.ycor()+50 and ball.ycor()>paddleL.ycor()-50):
        ball.dx *= -1
        ball.setx(-440)
