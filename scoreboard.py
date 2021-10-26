from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.score_refresh()

    def score_refresh(self):
        self.write(arg=f"Score : {self.score}", move=False, align="center", font=("Calibre", 18, "bold"))

    def update_score(self):
        self.increase_score()
        self.score_refresh()

    def increase_score(self):
        self.clear()
        self.score += 1

    def wall_hit(self):
        self.speed("fastest")
        self.home()
        self.write(arg="Game Over", move=False, align="center", font=("Calibre", 30, "bold"))
