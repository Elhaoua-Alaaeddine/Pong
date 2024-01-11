from turtle import Turtle


class Paddle(Turtle):

    def up(self):
        if self.ycor() > 230:
            return
        else:
            self.forward(40)

    def down(self):
        if self.ycor() < -230:
            return
        else:
            self.forward(-40)

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.setheading(90)
        self.shapesize(stretch_len=5)
        self.penup()
