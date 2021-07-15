# cook your dish here
t=int(input())
inputs=[]
for i in range(0,t):
 n,k=map(int,input().split())
 a=[]
 for i in range(n,0,-1):
  a.append(i)
 a[0:k+1]=reversed(a[0:k+1])
 print(*a)
