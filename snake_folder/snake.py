from turtle import Turtle, Screen
HOME_POSITIONS= [(0, 0), (20,0), (40,0)]
SPEED = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]
        self.move()
        self.up()
        self.down()
        self.left()
        self.right()

    def create_snake(self, ):
        for position in HOME_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
            new_turtle = Turtle("square")
            new_turtle.penup()
            new_turtle.color("black")
            new_turtle.goto(position)
            self.turtles.append(new_turtle)
        # self.turtles[0].color("brown")


    def snake_grow(self):
        self.add_segment(self.turtles[-1].position())





    def move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[i - 1].xcor()
            new_y = self.turtles[i - 1].ycor()
            self.turtles[i].goto(new_x, new_y)
        self.head.fd(SPEED)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

