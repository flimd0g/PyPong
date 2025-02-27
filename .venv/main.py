import turtle
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PyPong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    score.update()
    # Detect collision with floor and ceiling
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect right side missing
    if ball.xcor() > 400:
        ball.reset()
        score.l_point()
        score.update()

    # Detect left side missing
    if ball.xcor() < -400:
        ball.reset()
        score.r_point()
        score.update()

screen.exitonclick()