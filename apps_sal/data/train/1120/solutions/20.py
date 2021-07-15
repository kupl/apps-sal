# cook your dish here
t=int(input())
while t>0:
 r,c=list(map(int,input().split()))
 x,y=list(map(int,input().split()))
 x+=1 
 y+=1
 a=max(x-1,r-x)
 b=max(y-1,c-y)
 print(a+b)
 t-=1
 

