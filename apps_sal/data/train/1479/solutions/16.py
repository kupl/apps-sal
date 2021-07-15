T=int(input())
for i in range (T):
 n=int(input())
 l=[0]*11
 for i in range (n):
  X,Y=map(int,input().split())
  if X<9 and l[X-1]<Y:
   l[X-1]=Y
 print(sum(l)) 
