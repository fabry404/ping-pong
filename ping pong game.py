import turtle

window = turtle.Screen()
window.title("ping pong game")
window.bgcolor("black")
window.setup(width=800 , height=600)
window.tracer(0)

#player1
player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.color("blue")
player1.shapesize(stretch_wid=5 , stretch_len=1)
player1.penup()
player1.goto(-350 , 0)

#player2
player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.color("red")
player2.shapesize(stretch_wid=5 , stretch_len=1)
player2.penup()
player2.goto(350 , 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = .15
ball.dy = .15

#score
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0 , 260)
score.write("player1 ---> 0  || player2 ---> 0 " , align="center" , font=("Courier" , 24 , "normal"))
score1 = 0
score2 = 0

#functions

def player1_up():
    y = player1.ycor()
    y += 20
    player1.sety(y)

def player2_up():
    y = player2.ycor()
    y += 20
    player2.sety(y)

def player1_down():
    y = player1.ycor()
    y -= 20
    player1.sety(y)

def player2_down():
    y = player2.ycor()
    y -= 20
    player2.sety(y)


#keyboard keys

window.listen()
window.onkeypress(player1_up,"w")
window.onkeypress(player1_down,"s")
window.onkeypress(player2_up,"Up")
window.onkeypress(player2_down,"Down")



while True:
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0 , 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("player1 ---> {}  || player2 ---> {} ".format(score1 , score2), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0 , 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("player1 ---> {}  || player2 ---> {} ".format(score1, score2), align="center",
                    font=("Courier", 24, "normal"))

#collision between players

    if (ball.xcor() < -340 and ball.xcor() > -350) and  (ball.ycor() < player1.ycor() + 40 and ball.ycor() > player1.ycor()- 40 ):
        ball.setx(340)
        ball.dx *= -1


    if (ball.xcor() > 340 and ball.xcor() < 350) and  (ball.ycor() < player2.ycor() + 40 and ball.ycor() > player2.ycor()- 40 ):
        ball.setx(340)
        ball.dx *= -1



