# TODO 1 Create the snake body
from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Nokia 3310 Snake Game.")
screen.tracer(0)

screen.listen()
test = Snake()
screen.update()
food = Food()
score_board = Scoreboard()
score_board.score_refresh()
screen.onkey(key="w", fun=test.turn_up)
screen.onkey(key="s", fun=test.turn_down)
screen.onkey(key="d", fun=test.turn_right)
screen.onkey(key="a", fun=test.turn_left)


def wall_collision(snake):
    if snake.xcor() > 280 or snake.xcor() < -280 or snake.ycor() > 280 or snake.ycor() < -280:
        return True


def snake_tail_collision(snake_head):
    for seg in test.snake_segments[1:]:
        if snake_head.distance(seg) < 10:
            return True


game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    test.move()
    if test.snake_head.distance(food) <= 15:
        screen.tracer(0)
        test.snake_increase()
        food.food_generator()
        score_board.update_score()
    # TODO Remove the game_on and add reset current score and add it to High score
    # TODO Rest the snake segments to start from the home position
    if wall_collision(test.snake_head):
        score_board.wall_hit()
        game_on = False
    if snake_tail_collision(test.snake_head):
        score_board.wall_hit()
        game_on = False

screen.exitonclick()
