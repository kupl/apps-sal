import sys
import math
from collections import defaultdict,Counter

input=sys.stdin.readline
def print(x):
 sys.stdout.write(str(x)+"\n")

# sys.stdout=open("CP1/output.txt",'w')
# sys.stdin=open("CP1/input.txt",'r')

def power(x,y,m):
 if y==0:
  return 1
 p=power(x,y//2,m)%m
 p=(p*p)%m
 if y%2==0:
  return p
 else:
  return((x*p)%m)

def find(n,r):
 p=1
 q=1
 for j in range(1,r+1):
  p=(p*(n-j+1))%m
  q=(q*j)%m
 return (p*power(q,m-2,m))%m

m=pow(10,9)+7
t=int(input())
for i in range(t):
 n,m1=map(int,input().split())
 a=list(map(int,input().split()))
 avail=0
 req=m1-(n-1)
 ans=1
 c=Counter(a)
 for j in c:
  avail+=(c[j]*c[j-1])//2
  if j==1:
   continue
  ans=(ans*pow(c.get(j-1,0),c[j],m))%m
 if req>avail:
  print(0)
 else:
  ans=(ans*find(avail,req))%m
  print(ans)

