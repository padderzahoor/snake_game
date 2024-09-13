import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
score = 0



screen = Screen()
screen.setup(800, 800)
screen.bgcolor("gray")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard(score)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        score += 1
        scoreboard.update_score(score)
        food.refresh()
        snake.snake_grow()

    # Detect collision with wall
    if (snake.head.xcor() >= 400 or
            snake.head.xcor() <= -400 or
            snake.head.ycor() >= 400 or
            snake.head.ycor() <= -400):
        scoreboard.game_over()
        game_on = False

    # Collision with Body
    for segment in snake.turtles[3:]:
        if snake.head.distance(segment) < 10 and segment is not snake.head:
            game_on = False
            scoreboard.game_over()
            break  # Exit the loop if a collision is detected




screen.exitonclick()