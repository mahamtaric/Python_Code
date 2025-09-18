import turtle as t
import time
import random
screen=t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake_position=[(0,0),(-20,0),(-40,0)]




size=False
segments=[]
for x,y in snake_position:
    new_seg = t.Turtle("square")
    new_seg.color("green")
    new_seg.penup()
    new_seg.goto(x,y)
    segments.append(new_seg)
    
        


def right():
    segments[0].setheading(0)
def left():
    segments[0].setheading(180)
def up():
    segments[0].setheading(90)
def down():
    segments[0].setheading(270)

screen.listen()
screen.onkey(right,"d")
screen.onkey(left,"a")
screen.onkey(up,"w")
screen.onkey(down,"s")
    

border = t.Turtle()
border.hideturtle()
border.color("white")
border.penup()
border.goto(-300, 300)
border.pendown()
for _ in range(4):
    border.forward(600)
    border.right(90)

circleoffood=t.Turtle("circle")
circleoffood.shapesize(0.5)
circleoffood.penup()
random_food=(random.randint(-280,280),random.randint(-280,280))
circleoffood.goto(random_food)
circleoffood.color("white")
moves=0
game=True
while game==True:
    screen.update()
    time.sleep(0.1)
    distance=segments[0].distance(circleoffood)
    for x in range(len(segments)-1,0,-1):
        new_x=segments[x-1].xcor()
        new_y=segments[x-1].ycor()
        segments[x].goto(new_x,new_y)
    if distance<15:
        random_food=(random.randint(-280,280),random.randint(-280,280))
        circleoffood.goto(random_food)
        new_seg=t.Turtle("square")
        new_seg.color("green")
        new_seg.penup()
        segments.append(new_seg)
    segments[0].forward(20)
    if (segments[0].xcor() > 290 or segments[0].xcor() < -290 or
        segments[0].ycor() > 290 or segments[0].ycor() < -290):
        game = False
        print("Game Over! Snake hit the wall.")
    if moves>3:
        for x in segments[1:]:
            if segments[0].distance(x) < 1:
                game = False
                print("Game Over! Snake bit itself.")



screen.exitonclick()