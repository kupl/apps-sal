class Pong:
    def __init__(self,m):
        self.m,self.w=m,[0,0]
        self.o=self.p=0

    def play(self,b,a):
        if self.o:return "Game Over!"
        self.p+=1
        if abs(b-a)<3.5:return "Player %d has hit the ball!"%(2-self.p%2) 
        self.w[self.p%2]+=1
        if any(self.m<=x for x in self.w):self.o=1
        return "Player %d has %s!"%(2-(self.o+self.p)%2,('missed the ball','won the game')[self.o])
