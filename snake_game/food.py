from turtle import Turtle
import random

class Food(Turtle):              # hereda los metodos
    def __init__(self):
        # self.food = Turtle()
        super().__init__()       # hereda los atributos
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")


    def refresh(self):
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))





