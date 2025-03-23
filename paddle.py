from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1) #it becomes 100,20pxl
        self.penup()
        self.goto(position)

    def move_up(self):
        newy = self.ycor() +25
        self.goto(self.xcor(),newy)

    def move_down(self):
        newy = self.ycor() -25
        self.goto(self.xcor(),newy)



        
