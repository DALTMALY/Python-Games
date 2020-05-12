import turtle
import time
import random

Delay = 0.1

score = 0
high_score = 0

#Window Configuration
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600,height=600)
wn.tracer(0)

#Snake Head
snake_head = turtle.Turtle()
snake_head.speed(0)
snake_head.shape("square")
snake_head.color("white")
snake_head.penup()
snake_head.goto(0,0)
snake_head.direction = "stop"

#Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(random.randint(-280,240),random.randint(-280,240))
food.direction = "stop"

#Snake Body
snake_body = []

#Game Over
text = turtle.Turtle()
text.speed(0)
text.color("red")
text.penup()
text.hideturtle()
text.goto(0,260)
text.write("Score: 0        High Score: 0", align = "center", font = ("Courier",10, "normal"))

#Functions
def up():
    snake_head.direction = "up"
def down():
    snake_head.direction = "down"
def left():
    snake_head.direction = "left"
def right():
    snake_head.direction = "right"

def mov():
    if snake_head.direction=="up":
        y = snake_head.ycor()
        snake_head.sety(y+20)

    if snake_head.direction=="down":
        y = snake_head.ycor()
        snake_head.sety(y-20)

    if snake_head.direction=="left":
        x = snake_head.xcor()
        snake_head.setx(x-20)

    if snake_head.direction=="right":
        x = snake_head.xcor()
        snake_head.setx(x+20)

#Keyboard
wn.listen()
wn.onkeypress(up,"Up")
wn.onkeypress(down,"Down")
wn.onkeypress(left,"Left")
wn.onkeypress(right,"Right")


while True:
    wn.update()

    #Collisions edge
    if snake_head.xcor() > 290 or snake_head.xcor() < -290 or snake_head.ycor() > 280 or snake_head.ycor() < -290:
        time.sleep(1)
        snake_head.goto(0,0)
        snake_head.direction = "stop"

        #Hide Segments
        for part_body in snake_body:
            part_body.hideturtle()

        #Clean parts
        snake_body.clear()

        #Reset Score
        score = 0
        text.clear()
        text.write("Score: {}        High Score: {}".format(score, high_score), align = "center", font = ("Courier",10, "normal"))


    if snake_head.distance(food) < 20:
        x = random.randint(-280,240)
        y = random.randint(-280,240)
        food.goto(x,y)

        body_snake = turtle.Turtle()
        body_snake.speed(0)
        body_snake.shape("square")
        body_snake.color("grey")
        body_snake.penup()
        snake_body.append(body_snake)

        #Increase Score
        score += 10

        if score > high_score:
            high_score = score

        text.clear()
        text.write("Score: {}        High Score: {}".format(score, high_score), align = "center", font = ("Courier",10, "normal"))

    #Move Snake Body
    totalSeg = len(snake_body)
    for index in range(totalSeg-1,0,-1):
        x = snake_body[index -1].xcor()
        y = snake_body[index-1].ycor()
        snake_body[index].goto(x,y)

    if totalSeg > 0:
        x = snake_head.xcor()
        y = snake_head.ycor()
        snake_body[0].goto(x,y)


    mov()

    #Body Collisions
    for part_body in snake_body:
        if part_body.distance(snake_head) < 20:
            time.sleep(1)
            snake_head.goto(0,0)
            snake_head.direction = "stop"

            for part_body in snake_body:
                part_body.hideturtle()
            
            snake_body.clear()

            #Reset Score
            score = 0
            text.clear()
            text.write("Score: {}        High Score: {}".format(score, high_score), align = "center", font = ("Courier",10, "normal"))



    time.sleep(Delay)


input("Press a Key to exit...")