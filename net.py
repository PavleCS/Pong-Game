from turtle import Turtle
PEN_SIZE = 4


class Net(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.pensize(PEN_SIZE)
        self.line_drawing()

    def line_drawing(self):
        self.penup()
        self.setposition(0, 290)
        self.setheading(270)
        while self.ycor() > -290:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)

