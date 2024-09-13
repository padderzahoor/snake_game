from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, score):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-70, 350)
        self.write(f"Your Score is : {score}", False, font=('Arial', 15, 'normal'))

    def update_score(self, score):
        self.clear()
        self.write(f"Your Score is : {score}", False, font=('Arial', 15, 'normal'))

    def game_over(self):
        self.goto(-70, 0)
        self.write(f"GAME OVER", False, font=('Arial', 15, 'normal'))