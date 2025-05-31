from turtle import Turtle

FONT = ("Courier", 18, "normal")

# Esta clase lleva el marcador, el numero del nivel y el game over
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_screen()

    def update_screen(self):
        self.clear()
        self.goto(-220, 260)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def next_level(self):
        self.level += 1
        self.update_screen()

    def game_over(self):
        self.update_screen()
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)










