import sys

t=int(sys.stdin.readline())
x='RGB'
y='GBR'
z='BRG'
# x='RGB'
for i in range(t):
    n,k=list(map(int,sys.stdin.readline().strip().split()))
    a=sys.stdin.readline().strip()
    xk=x
    yk=y
    zk=z
   
    op=2001
    
    xd=[]
    yd=[]
    zd=[]
    xdc=0
    ydc=0
    zdc=0
    b=a
    for j in range(k):
        if(b[j]!=xk[j%3]):
            xd.append(1)
            xdc+=1
        else:
            xd.append(0)
            
        if(b[j]!=yk[j%3]):
            yd.append(1)
            ydc+=1
        else:
            yd.append(0)
            
        if(b[j]!=zk[j%3]):
            zdc+=1
            zd.append(1)
        else:
            zd.append(0)
    op=min(xdc,ydc,zdc)
    
    for j in range(k,n):
        # print(b,len(b),j,xk)
        if(b[j]!=xk[j%3]):
            xd.append(1)
            xdc+=1
        else:
            xd.append(0)
            
        if(b[j]!=yk[j%3]):
            yd.append(1)
            ydc+=1
        else:
            yd.append(0)
            
        if(b[j]!=zk[j%3]):
            zdc+=1
            zd.append(1)
        else:
            zd.append(0)
        # print("here")
        xdc-=xd[j-k]
        ydc-=yd[j-k]
        zdc-=zd[j-k]
        op=min(op,xdc,ydc,zdc)
    print(op)
    
#oh , had been testing with other test case, first had set only x, but then added back y and z :P

