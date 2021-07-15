# cook your dish here
import math
for _ in range(int(input())):
 n=int(input())
 x=0
 for i in range(n):
  l=list(map(int,input().split()))
  c=l[0]
  l1=l[1:]
  d=math.ceil(c/2)
  for i in range(d):
   x=x+l1[i]
  l1=[]
  c=0
  d=0
 print(x)

