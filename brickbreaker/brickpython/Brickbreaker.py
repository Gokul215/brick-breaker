import time
import sys

class Brickbreaker:
    wall="w"
    ground='g'
    brick='1'
    ball='o'
    bricksWithLife={}
    balllife=5
    def __init__(self,row,col) -> None:
        self.row=row 
        self.col=col 
        self.brickoard=[[0]*col for i in range(row)]
        self.prepare()
        self.brickoard[row-1][col//2]=Brickbreaker.ball
        self.ballpos=[row-1,col//2]
    def prepare(self):
        for i in range(self.row):
            for j in range(self.col):
                if i==0 or j==0 or j==self.col-1:
                    self.brickoard[i][j]=Brickbreaker.wall
                elif i==self.row-1:
                    self.brickoard[i][j]=Brickbreaker.ground
                else:
                    self.brickoard[i][j]=' '
            
    def printboard(self):
        print("-----------------------------")
        for i in range(len(self.brickoard)):
            for j in range(len(self.brickoard[0])):
                print(self.brickoard[i][j], end=' ')
            print()
    def placeBricks(self,row,col,life):
        self.brickoard[row][col]=Brickbreaker.brick
        Brickbreaker.bricksWithLife[(row,col)] = life
        
    def initiateBall(self):
        i=len(self.brickoard)-1
        for j in range(1,len(self.brickoard[0])-1):
            if self.brickoard[i][j] != Brickbreaker.ball:
                self.brickoard[i][j]=Brickbreaker.ground
                
    def movedirection(self,ballx,bally,movex,movey):
        self.initiateBall()
        while self.brickoard[ballx][bally] != Brickbreaker.wall:
            if self.brickoard[ballx][bally] == Brickbreaker.brick:
                self.goesdown(ballx,bally)
                return
            self.illusion(ballx,bally)
            ballx+=movex
            bally+=movey
            # print(ballx,bally,'ball')
        # print(ballx,bally,'w')
        self.wallHit(ballx,bally)
        movex=0
        movey*=-1
        if movey==0:
            self.goesdown(ballx+1,bally)
        else:

            self.movedirection(ballx,bally+movey,movex,movey)
        
    def wallHit(self,x,y):
        # print(x,y,'wall')
        self.brickoard[x][y]=Brickbreaker.ball
        self.printboard()
        self.brickoard[x][y]=Brickbreaker.wall
        self.sleepforone()
        
        
    def illusion(self,ballx,bally):
        if self.brickoard[ballx][bally]==Brickbreaker.brick:
            self.reducebrickandballlife(ballx,bally)
            
        else:
            self.brickoard[ballx][bally]=Brickbreaker.ball
            # print("g")
            self.printboard()
            self.brickoard[ballx][bally]=' '
            self.sleepforone()
            if Brickbreaker.balllife <1:
                print("game over----")
                print("Exiting program.")
                sys.exit(0)
        
    def goesdown(self,ballx,bally):
        while ballx != len(self.brickoard):
            self.illusion(ballx,bally)
            ballx+=1
        self.ballpos=[ballx-1,bally]
        print(self.ballpos[0])
        self.brickoard[self.ballpos[0]][self.ballpos[1]]=Brickbreaker.ball
        
    def reducebrickandballlife(self,x,y):
        # print(x,y)
        if Brickbreaker.balllife >=1:
            Brickbreaker.bricksWithLife[(x,y)] -=1
            
        Brickbreaker.balllife-=1
        
        if Brickbreaker.bricksWithLife[(x,y)]<=0:
            self.brickoard[x][y]=' '
        
        
        
    def sleepforone(self):
        time.sleep(1)
        
        
        
        