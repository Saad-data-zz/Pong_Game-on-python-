from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        #creating attributes of score
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        #the scireboard updated but it's over written, to avoid that we use
        self.clear()
        # position of the score board
        self.goto(-100, 200)
        # writing the score on screen
        self.write(self.l_score, align="center", font=("Counier", 80, "normal"))
        # for the r_score borad
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Counier", 80, "normal"))


    def l_point(self):
            self.l_score += 1
            self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
