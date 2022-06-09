from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.setposition(0, 270)
        self.write(arg=f"Score: {self.score}", move=False, align='center', font=('Courier', 15, 'normal'))

    def refresh(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}", move=False, align='center', font=('Courier', 15, 'normal'))

    def game_over(self):
        self.setposition(0, 0)
        self.write(arg='Game Over.', move=False, align='center', font=('Courier', 15, 'normal'))