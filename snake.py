from turtle import Turtle

DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
segments = 3
POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.snake_head = self.snake_segments[0]

    def create_snake(self):
        for pos in POSITION:
            self.add_segments(pos)

    def move(self):
        for seg in range(len(self.snake_segments) - 1, 0, -1):
            self.snake_segments[seg].showturtle()
            new_x = self.snake_segments[seg - 1].xcor()
            new_y = self.snake_segments[seg - 1].ycor()
            self.snake_segments[seg].goto(new_x, new_y)
        self.snake_segments[0].forward(DISTANCE)

    def snake_increase(self):
        pos = self.snake_segments[-1].pos()
        self.add_segments(pos)

    def add_segments(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.snake_segments.append(segment)

    def turn_up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def turn_down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def turn_right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def turn_left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def rest_snake(self):
        #This soluation is much better than mine because the snake segments dissappera and
        #the snake initialize much faster on the screen
        for seg in self.snake_segments:
            seg.goto(1000, 1000)
        self.snake_segments.clear()
        self.create_snake()
        self.snake_head = self.snake_segments[0]
        #This my soluation
        # for seg in self.snake_segments[3:]:
        #     seg.hideturtle()
        # self.snake_segments = self.snake_segments[0:3]
        # self.snake_head.goto(0, 0)




