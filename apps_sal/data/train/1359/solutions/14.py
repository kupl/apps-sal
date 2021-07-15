import sys
import math
from collections import defaultdict,Counter

input=sys.stdin.readline
def print(x):
 sys.stdout.write(str(x)+"\n")

# sys.stdout=open("CP1/output.txt",'w')
# sys.stdin=open("CP1/input.txt",'r')

# mod=pow(10,9)+7
t=int(input())
for i in range(t):
 n=int(input())
 a=list(map(int,input().split()))
 od=0
 for j in a:
  if j&1:
   od+=1
 ev=n-od
 ans=min(max(0,(od-1))*2+ev,max(0,(ev-1))*2+od)
 print(ans)

