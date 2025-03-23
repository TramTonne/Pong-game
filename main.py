from turtle import Turtle, Screen
from paddle import Paddle
from pong import Pong
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.title("Tram's Pong Game")
screen.tracer(0)

right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))

#make the screen listen to the corresponding key put
#make this infront of the game_on
screen.listen()
screen.onkey(right_paddle.move_down,"Down")
screen.onkey(right_paddle.move_up,"Up")
screen.onkey(left_paddle.move_down,"s")
screen.onkey(left_paddle.move_up,"w")

#create pong
pong=Pong()
scoreboard = ScoreBoard()
game_on = True
while game_on:
    time.sleep(pong.move_speed)
    screen.update()
    pong.move()

    #detect ball collision with the top and bottom walls
    if pong.ycor()>280 or pong.ycor()<-280:
        pong.wall_bounce()

    #detect the paddle collision
    #check 2 conditions: pong's xcor greater than 330 and the distance from the pong to the center of paddle less than 50
    if pong.distance(right_paddle) <50 and pong.xcor()>320:
        pong.paddle_bounce()
    if pong.distance(left_paddle) <50 and pong.xcor()<-320:
        pong.paddle_bounce()
    #detect if the pong goes out of bound:
    #if the pong goes out then it will be reset the position, if it touch the right-ended side than it has to start moving toward the left
    if pong.xcor()>380:
        pong.reset_position()
        scoreboard.update_lscore()

    if pong.xcor()<-380:
        pong.reset_position()
        scoreboard.update_rscore()
screen.exitonclick()