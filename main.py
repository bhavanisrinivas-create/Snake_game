from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time
scr=Screen()
scr.tracer(0)
scr.setup(height=600,width=600)
scr.bgcolor('black')
snake=Snake()
food=Food()
score=Score()
scr.listen()
scr.onkeypress(key='Up',fun=snake.moveUp)
scr.onkeypress(key='Down',fun=snake.moveDown)
scr.onkeypress(key='Right',fun=snake.moveRight)
scr.onkeypress(key='Left',fun=snake.moveLeft)


sleep_time=0.1
while True:
    snake.snakeMove()
    scr.update()
    time.sleep(sleep_time)
    if snake.collided(food):#if collided
        #put the food to another random location
        food.refresh()
        #increase the length of snake
        snake.increaseLength()
        #increase speed
        # sleep_time/=2
        score.increaseScore()
    head=snake.segments[0]
    #Detecting collision with the boundaries
    x=head.xcor()
    y=head.ycor()
    if x>300:
        head.setpos(-300,y)
    if x<-300:
        head.setpos(300,y)
    if y>300:
        head.setpos(x,-300)
    if y<-300:
        head.setpos(x,300)    
    
    #Detect collision with snakebody
    if snake.hasCollidedWithBody():
        break
        
scr.exitonclick()