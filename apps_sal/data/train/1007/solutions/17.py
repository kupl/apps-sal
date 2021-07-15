# cook your dish here
import functools
t=int(input())

def gcdn(s,n):
 
 def gcd(x,y):
  while y:
   x,y=y,x%y
  return x
   
 t=functools.reduce(lambda x,y:gcd(x,y),s)
  
 if t==1:
  return n
   
 else:
  return -1
  
 
for _ in range(t):
 
 n=int(input())
 s=list(map(int,input().split()))
 r=gcdn(s,n)
 print(r)
