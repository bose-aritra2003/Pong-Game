from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 80, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.left_score = 0
        self.right_score = 0
        self.penup()
        self.goto(0, 210)
        self.showScore()

    def showScore(self):
        """
        To display the score on the screen and clear the last score when score is updated
        """
        self.clear()
        self.write(f"{self.left_score} - {self.right_score}", align=ALIGNMENT, font=FONT)

    def increaseRightScore(self):
        """
        Increase a point of the right paddle player
        """
        self.right_score += 1
        self.showScore()

    def increaseLeftScore(self):
        """
        Increase a point of the left paddle player
        """
        self.left_score += 1
        self.showScore()
