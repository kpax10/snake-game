from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(0, 280)
        self.color('white')
        self.show_score()

    def show_score(self):
        self.write(arg=f'Score: {self.score}', align='center', font=('Arial', 20, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg='GAME OVER', align='center', font=('Arial', 40, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.show_score()
