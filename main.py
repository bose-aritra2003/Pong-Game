# Pong Game

# Based on the old school legendary pong game
# Read more at https://en.wikipedia.org/wiki/Pong

from scoreboard import Scoreboard
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

my_screen = Screen()
my_screen.title("Pong Game")
my_screen.bgcolor("black")
my_screen.setup(width=800, height=600)
my_screen.tracer(False)  # To not show the screen contents until all the subjects are rendered on the screen

my_left_paddle = Paddle(1)  # Left paddle
my_right_paddle = Paddle(2)  # Right paddle
my_ball = Ball()
my_scoreboard = Scoreboard()

my_screen.listen()
my_screen.onkey(fun=my_left_paddle.moveUp, key="w")
my_screen.onkey(fun=my_right_paddle.moveUp, key="Up")
my_screen.onkey(fun=my_left_paddle.moveDown, key="s")
my_screen.onkey(fun=my_right_paddle.moveDown, key="Down")

is_game_on = True
while is_game_on:
    time.sleep(my_ball.move_speed)
    my_screen.update()  # Shows the contents on the screen which were previously hidden by turning off the tracer
    my_ball.move()

    # Detecting collision of ball with top and bottom walls
    wall_collision = (my_ball.ycor() > 280 or my_ball.ycor() < -280)
    if wall_collision:
        my_ball.bounceWall()

    # Detecting collision of ball with left paddle
    left_paddle_collision = my_ball.xcor() < -320 and my_ball.distance(my_left_paddle) < 50
    if left_paddle_collision:
        my_ball.bounceLeftPaddle()

    # Detecting collision of ball with right paddle
    right_paddle_collision = my_ball.xcor() > 320 and my_ball.distance(my_right_paddle) < 50
    if right_paddle_collision:
        my_ball.bounceRightPaddle()
        
    # Detecting a miss by the right paddle
    missed_paddle = my_ball.xcor() > 380
    if missed_paddle:
        my_scoreboard.increaseLeftScore()
        my_ball.resetBall()

    # Detecting a miss by the left paddle
    missed_paddle = my_ball.xcor() < -380
    if missed_paddle:
        my_scoreboard.increaseRightScore()
        my_ball.resetBall()


my_screen.exitonclick()
