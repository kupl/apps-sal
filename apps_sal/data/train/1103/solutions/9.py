from collections import *
def prime(n):
 d=2
 while d*d<=n:
  while n%d==0:
   primef.append(d)
   n=n//d
  d+=1
 if n>1: primef.append(n)
for _ in range(eval(input())):
 primef=[]
 x,prod=eval(input()),1
 m=list(map(int,input().split()))
 for i in m:
  prime(i)
 for i in primef:
  if primef.count(i)>=2: break
 print(i)

