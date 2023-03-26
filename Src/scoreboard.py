from turtle import Turtle


with open('High_Score.txt', mode='r') as file:
    High_Score = int(file.read())


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.setposition(0, 270)
        self.write(arg=f"Score: {self.score}  High Score: {High_Score}", move=False, align='center', font=('Courier', 15, 'normal'))

    def refresh(self):
        self.clear()
        self.write(arg=f"Score: {self.score}  High Score: {High_Score}", move=False, align='center', font=('Courier', 15, 'normal'))

    def reset(self):
        global High_Score
        if self.score > High_Score:
            with open('High_Score.txt', mode='w') as File:
                File.write(str(self.score))
            with open('High_Score.txt') as File:
                High_Score = int(File.read())
        self.score = 0
        self.refresh()

    def increase_score(self):
        self.score += 1
