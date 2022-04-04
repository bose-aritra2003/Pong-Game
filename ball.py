from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("red")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """
        To move the ball on the screen
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounceWall(self):
        """
        To make the ball bounce from the top and bottom walla
        """
        self.y_move *= -1

    def bounceLeftPaddle(self):
        """
        To make the ball bounce from the left paddle
        """
        self.x_move = (abs(self.x_move))
        self.move_speed *= 0.9

    def bounceRightPaddle(self):
        """
        To make the ball bounce from the right paddle
        """
        self.x_move = -(abs(self.x_move))
        self.move_speed *= 0.9

    def resetBall(self):
        """
        To reset the position of the ball back to the center of the screen and
        to reverse the direction in which it last started moving
        """
        self.home()
        self.move_speed = 0.1
        self.x_move *= -1
        self.y_move *= -1