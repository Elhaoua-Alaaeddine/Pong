from turtle import Turtle, Screen
from ball import Ball
from scoreboard import Scoreboard
from paddle import Paddle
import time

STARTING_POSITIONS = [(350, 0), (-350, 0)]


def draw_middle_line():
    middle_line = Turtle()
    middle_line.ht()
    middle_line.penup()
    middle_line.color("white")
    middle_line.speed("fastest")
    middle_line.goto(x=0, y=270)
    middle_line.pensize(10)
    middle_line.setheading(270)
    for x in range(27):
        if x % 2 == 0:
            middle_line.pendown()
        else:
            middle_line.penup()
        middle_line.forward(20)


def paddles_setup():
    p1.goto(STARTING_POSITIONS[0])
    p2.goto(STARTING_POSITIONS[1])
    p1.speed("fast")
    p2.speed("fast")


s = Screen()

s.setup(width=800, height=600)
s.bgcolor("black")
s.title("Pong")
s.listen()
s.tracer(0)
score = Scoreboard()
b = Ball()
p1 = Paddle()
p2 = Paddle()
score.write_score()
paddles_setup()
draw_middle_line()
s.onkeypress(p1.up, "Up")
s.onkeypress(p1.down, "Down")
s.onkeypress(p2.up, "w")
s.onkeypress(p2.down, "s")

done = False
left_to_right = True
while not done:
    s.update()
    time.sleep(0.05)
    b.move()
    if b.ycor() > 280 or b.ycor() < -280:
        b.bounce_y()
    if b.distance(p1) < 50 and b.xcor() > 320 and left_to_right:
        left_to_right = False
        b.bounce_x()
    elif b.distance(p2) < 50 and b.xcor() < -320 and not left_to_right:
        left_to_right = True
        b.bounce_x()
    elif b.xcor() > 400:
        del b
        score.refresh_p1()
        b = Ball()
        b.bounce_x()
        left_to_right = False
    elif b.xcor() < -400:
        del b
        score.refresh_p2()
        b = Ball()
        left_to_right = True

s.exitonclick()
