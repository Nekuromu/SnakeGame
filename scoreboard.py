from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.color("white")
        self.penup()
        self.goto(0, 275)
        self.increase_score()
        self.hideturtle()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER.", False, align=ALIGNMENT, font=FONT)
