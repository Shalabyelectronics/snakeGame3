# TODO 1 Create the snake body
from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time
import os.path

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Nokia 3310 Snake Game.")
screen.tracer(0)

screen.listen()
snake = Snake()
screen.update()
food = Food()
score_board = Scoreboard()

if os.path.isfile("./highest_score.txt"):
    with open("./highest_score.txt") as track_score:
        temp = track_score.read()
        if temp:
            content = int(temp)
            score_board.highest_score = content
        else:
            score_board.highest_score = 0
        
else:
    with open("./highest_score.txt", mode="w") as track_score:
        content = track_score.write(str(score_board.highest_score))

score_board.score_refresh()
screen.onkey(key="w", fun=snake.turn_up)
screen.onkey(key="s", fun=snake.turn_down)
screen.onkey(key="d", fun=snake.turn_right)
screen.onkey(key="a", fun=snake.turn_left)


def wall_collision(snake_player):
    if snake_player.xcor() > 280 or snake_player.xcor() < -280 \
            or snake_player.ycor() > 280 or snake_player.ycor() < -280:
        return True


def snake_tail_collision(snake_head):
    for seg in snake.snake_segments[1:]:
        if snake_head.distance(seg) < 10:
            return True


game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.snake_head.distance(food) <= 15:
        screen.tracer(0)
        snake.snake_increase()
        food.food_generator()
        score_board.update_score()
        with open("./highest_score.txt", mode="w") as track_score:
            content = track_score.write(str(score_board.highest_score))
    # TODO Remove the game_on and add reset current score and add it to High score
    # TODO Rest the snake segments to start from the home position
    if wall_collision(snake.snake_head):
        score_board.reset_score()
        snake.rest_snake()
    if snake_tail_collision(snake.snake_head):
        score_board.reset_score()
        snake.rest_snake()

screen.exitonclick()
