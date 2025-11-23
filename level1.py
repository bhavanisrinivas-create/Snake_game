from turtle import Turtle,Screen


screen=[[1,1,1,1,1,1,1,1,1,1],
 [1,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,1],
 [1,0,0,0,0,0,0,0,0,1],
 [1,1,1,1,1,1,1,1,1,1]
 ]
scr=Screen()
scr.setup(height=600,width=600)
for i in range(len(screen)):
    for j in range(len(screen)):
        if screen[i][j]==1:
            t=Turtle()
            t.shape('square')
            # t.shapesize(stretch_len=2,stretch_wid=2)
            t.setpos(-280+i*20,280-j*20)
scr.exitonclick()           