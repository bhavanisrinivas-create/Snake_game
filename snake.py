from turtle import Turtle
INITIAL_POSITION=[
    (0,0),(-20,0),(-40,0)
]
class Snake:
    def __init__(self):
        self.segments=[]#Accessing all segment
        self.drawSnake()
    def drawSnake(self):
        for pos in INITIAL_POSITION:#create segments
            segment=Turtle()
            segment.color('white')
            segment.shape('square')
            segment.penup()
            segment.setpos(pos)
            self.segments.append(segment)
    def snakeMove(self):
        for i in range(len(self.segments)-1,0,-1):
            prev_seg=self.segments[i-1]
            prev_x=prev_seg.xcor()  
            prev_y=prev_seg.ycor()
            self.segments[i].setpos(prev_x,prev_y)   
        self.segments[0].forward(20)   
    def moveUp(self):
        if self.segments[0].heading()!=270:
            self.segments[0].setheading(90)
    def moveDown(self):
        if self.segments[0].heading()!=90:
            self.segments[0].setheading(270) 
    def moveRight(self):
        if self.segments[0].heading()!=180:
            self.segments[0].setheading(0)
    def moveLeft(self):
        if self.segments[0].heading()!=0:
            self.segments[0].setheading(180) 
    #detecting the collision     
    def collided(self,food):#head=segments[0]
        if self.segments[0].distance(food)<=20:
            return True
        else:
            return False     
    def increaseLength(self):
        newSegment=Turtle()
        newSegment.penup()
        newSegment.shape('square')
        newSegment.color('white')
        x=self.segments[-1].xcor()
        y=self.segments[-1].ycor()
        newSegment.setpos(x,y)
        self.segments.append(newSegment)  
    def hasCollidedWithBody(self):
        head=self.segments[0]
        for i in range(2,len(self.segments)):#looping through allbody parts except head
            if head.distance(self.segments[i])<20:#testing for collision
                return True
        return False
        