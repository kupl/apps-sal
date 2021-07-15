# cook your dish here
t=int(input())
for i in range(t):
 x,y,k=map(int,input().split())
 a=x+y
 b=a//k
 if b%2==0:
  print("Chef")
 else:
  print("Paja")
