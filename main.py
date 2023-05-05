from turtle import Screen
from net import Net
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time


net = Net()
score = Scoreboard()
paddle = Paddle()
ball = Ball()


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.listen()

screen.onkey(paddle.go_up1, "w")
screen.onkey(paddle.go_down1, "s")
screen.onkey(paddle.go_up2, "Up")
screen.onkey(paddle.go_down2, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move_ball()

#     Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

#     Collision with a paddle
    if ball.distance(paddle.paddle2) < 50 and ball.xcor() > 320 or ball.distance(paddle.paddle1) < 50 and \
            ball.xcor() < -320:
        ball.bounce_x()

    if ball.distance(paddle.paddle2) > 50 and ball.xcor() > 380:
        score.l_point()
        ball.reset()

    if ball.distance(paddle.paddle1) > 50 and ball.xcor() < -380:
        score.r_point()
        ball.reset()













screen.exitonclick()