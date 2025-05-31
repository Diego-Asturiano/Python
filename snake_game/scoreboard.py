from turtle import Turtle

ALIGNMENT = "center"

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        #self.high_score = 0
        with open("data.txt") as score_data:
             self.high_score= int(score_data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_screen()

    def update_screen(self):
        self.clear()
        self.write(f"Score: {self.points}  High Score: {self.high_score}", align=ALIGNMENT, font=("Arial", 12, "normal"))

    def reset(self):
        if self.points > self.high_score:
            self.high_score = self.points
            with open("data.txt", mode="w") as score_data:
                score_data.write(str(self.high_score))

        self.points = 0
        self.update_screen()

    #def game_over(self):
    #    self.goto(0,0)
    #    self.write("GAME OVER", align=ALIGNMENT, font=("Arial", 12, "normal"))

    def increase_score(self):
        self.points += 1
        self.update_screen()
