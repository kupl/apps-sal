n=int(input())
ta,tb,da,db=[0]*4
for i in range (n):
    t,x,y=list(map(int,input().split()))
    if t==1:
        ta+=(x+y)
        da+=y
    if (t==2):
        tb+=(x+y)
        db+=y       
if (ta-da>=0.5*ta):
    print ('LIVE')
else :
    print ('DEAD')
if (tb-db>=0.5*tb):
    print ('LIVE')
else :
    print ('DEAD')    
    

