for _ in range(int(input())):
 n=int(input())
 n=n*4-1
 x=0
 y=0
 for z in range(n):
  a,b=list(map(int,input().split()))
  x^=a
  y^=b
 print(x,y)

