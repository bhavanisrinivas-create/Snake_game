from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('yellow')
        self.score=0
        self.penup()
        self.hideturtle()
        self.setpos(-60,260)
        self.drawScoreBoard()
    
    def drawScoreBoard(self):
        self.write(f'Your Score is {self.score}',font=('Arial',20))
        
    def increaseScore(self):
        self.clear()
        self.score+=1
        self.drawScoreBoard()
        