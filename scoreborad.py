from turtle import Turtle
ALIGMNET="center"
FONT=('Arial', 24, 'normal')
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score= int(data.read())

        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreborad()

    def reset(self):
        global content
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode='w') as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreborad()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over ", align='center', font=FONT)

    def update_scoreborad(self):
        self.clear()
        self.write(f"Score {self.score}  High Score {self.high_score}", align=ALIGMNET, font=FONT)

    def increase_score(self):
        self.score += 1

        self.update_scoreborad()


