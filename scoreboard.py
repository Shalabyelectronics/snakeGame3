from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.highest_score = 0
        self.score = 0
        self.score_refresh()

    def score_refresh(self):
        self.clear()
        self.write(arg=f"Score : {self.score} | Highest score : {self.highest_score}", move=False, align="center",
                   font=("Calibre", 18, "bold"))

    def update_score(self):
        self.score += 1
        self.update_highest_score()
        self.score_refresh()

    def update_highest_score(self):
        if self.highest_score < self.score:
            self.highest_score = self.score
            self.score_refresh()

    def reset_score(self):
        self.update_highest_score()
        self.score = 0
        self.score_refresh()

