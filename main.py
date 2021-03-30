from turtle import  Screen

from paddle import Paddle
from ball import Ball
import time

from score import Score

screen = Screen()

screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)

score = Score()
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
screen.listen()
screen.onkey(key='Up', fun=r_paddle.go_up)
screen.onkey(key='Down', fun=r_paddle.go_down)
screen.onkey(key='w', fun=l_paddle.go_up)
screen.onkey(key='s', fun=l_paddle.go_down)
game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()
    if ball.xcor() > 360:
        ball.reset()
        score.l_point()

    if ball.xcor() < -360:
        ball.reset()
        score.r_point()

screen.exitonclick()
