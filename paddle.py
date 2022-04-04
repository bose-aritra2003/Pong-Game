from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, player_num):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        if player_num == 1:
            self.x = -350
        else:
            self.x = 350
        self.goto(self.x, 0)
        self.color("yellow")

    def moveUp(self):
        """
        To move the turtle towards north
        """
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def moveDown(self):
        """
        To move the turtle towards south
        """
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

