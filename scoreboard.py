from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.hideturtle()
        self.right_player=0
        self.left_player=0
        self.scoredisplay()

    #display scoreboard on top:
    def scoredisplay(self):
        self.write(f"Player1: {self.left_player} | Player2: {self.right_player}",align="center",font=("Courier",20,"normal"))
    
    #update score when pong goes out of bound
    def update_rscore(self):
        self.right_player+=1
        self.clear()
        self.scoredisplay()
    def update_lscore(self):
        self.left_player+=1
        self.clear()
        self.scoredisplay()