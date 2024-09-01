import turtle
from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreborad import Scoreboard


screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")

screen.tracer(0)

snake = Snake()
screen.listen()
food = Food()
scoreboard = Scoreboard()



screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

is_game_on= True
while is_game_on:
    screen.update()

    time.sleep(0.10)
    snake.move()


    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()



    #Detect collision with tail
    for sagment in snake.sagments[1:]:
        if snake.head.distance(sagment) <10:
            scoreboard.reset()
            snake.reset()





#         Or
# turtle1=Turtle()
# turtle2=Turtle()
# turtle3=Turtle()
# turtle2.color("white")
# turtle3.color("white")
# turtle1.color("white")
# turtle1.shape("square")
# turtle2.shape("square")
# turtle3.shape("square")
#
# turtle2.goto(x=-20,y=0)
# turtle3.goto(x=-40,y=0)
turtle.exitonclick()














