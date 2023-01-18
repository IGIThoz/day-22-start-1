import turtle as t
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

# 198 Setup Screen
WIDTH = 800
HEIGHT = 600
screen = t.Screen()
screen.bgcolor("black")
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("Pong")
screen.tracer(0)
# 205 Score Keeping and Changing the Ball Speed
scoreboard = ScoreBoard()

#  199 Create a Paddle
#  200 Write the Paddle Class an Create the Second Paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
game_on = True


def exit_game():
    global game_on, screen
    game_on = False
    screen.bye()


screen.listen()
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(exit_game, "p")
#  201 Write the Ball Class and Make The Ball Move
ball = Ball()

while game_on:
    screen.update()
    time.sleep(ball.speed)
    ball.move()
    # 202 Add the Ball Bouncing Logic
    # detect wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #  203 Detect collisions with the Paddle
        # detect collisions with r_paddle and l_paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or (ball.distance(l_paddle) < 50 and ball.xcor() < -340):
        ball.bounce_x()

    #  204 Detect when the Ball goes Out of Bounds
    if ball.xcor() > 380:
        #print("Left win")
        ball.reset_position()
        scoreboard.l_score_update()

    elif ball.xcor() < -380:
        #print("Right win")
        ball.reset_position()
        scoreboard.r_score_update()
