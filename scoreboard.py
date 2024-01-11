from turtle import Turtle


class Scoreboard(Turtle):
    def refresh_p1(self):
        self.p1_score += 1
        self.clear()
        self.write_score()

    def refresh_p2(self):
        self.p2_score += 1
        self.clear()
        self.write_score()

    def write_score(self):
        self.write(arg=f"{self.p1_score}    {self.p2_score}", align="center", font=("Arial", 60, "bold"))

    def __init__(self):
        super().__init__()
        self.ht()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(x=0, y=210)
        self.p1_score = 0
        self.p2_score = 0
