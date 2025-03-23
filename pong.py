from turtle import Turtle

class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move=10
        self.y_move=10
        self.move_speed = 0.1

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x= self.xcor()+ self.x_move
        self.goto(new_x,new_y)

    def wall_bounce(self):
        # self.x_move*=-1
        self.y_move*=-1 #reverse y only !!

    def paddle_bounce(self):
        self.x_move*=-1
        self.move_speed*=0.9

    def reset_position(self):
        self.goto(0,0)
        #reverse the direction of the pong when hit the sides
        self.x_move*=-1
        #remember to reset the speed too
        self.move_speed=0.1
    