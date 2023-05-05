from turtle import Turtle
STARTING_POSITIONS = [(-350, 0), (350, 0)]


class Paddle:

    def __init__(self):
        self.paddles = []
        self.starting_position()
        self.paddle1 = self.paddles[0]
        self.paddle2 = self.paddles[1]

    def starting_position(self):
        for position in STARTING_POSITIONS:
            self.create_paddle(position)

    def create_paddle(self, position):
        new_paddle = Turtle("square")
        new_paddle.penup()
        new_paddle.color("white")
        new_paddle.shapesize(stretch_wid=4, stretch_len=0.7)
        new_paddle.speed("fastest")
        new_paddle.goto(position)
        self.paddles.append(new_paddle)

    def go_up1(self):
        new_y = self.paddle1.ycor() + 20
        self.paddle1.goto(self.paddle1.xcor(), new_y)

    def go_down1(self):
        new_y = self.paddle1.ycor() + -20
        self.paddle1.goto(self.paddle1.xcor(), new_y)

    def go_up2(self):
        new_y = self.paddle2.ycor() + 20
        self.paddle2.goto(self.paddle2.xcor(), new_y)

    def go_down2(self):
        new_y = self.paddle2.ycor() + -20
        self.paddle2.goto(self.paddle2.xcor(), new_y)
