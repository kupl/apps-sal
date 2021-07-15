n= int(input())
l=[]
x=0
y=0
for i in range(n):
    a,b= map(int,input().split())
    x=x+a
    y=y+b
    l.append(x-y)
q=abs(max(l))
w=abs(min(l))
if w>q:
    r=2 
    q=w
else:
    r=1 
r=[r,q]
for p in r:
    print(p,end=' ')
