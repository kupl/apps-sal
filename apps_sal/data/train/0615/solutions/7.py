# cook your dish here
n=int(input())
for i in range(n):
 a,b=input().split()
 b=int(b)
 l=list(map(int,input().split()))
 x=[0]
 for j in l: 
  x.append(x[-1]+j)
 for j in range(b):
  e,f=input().split()
  print(x[int(f)]-x[int(e)-1])

