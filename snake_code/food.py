from turtle import Turtle, Screen
import random




class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("red")
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.speed(0)
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        self.goto(x, y)
        self.refresh()

    def refresh(self):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        self.goto(x, y)



