from sys import stdin, stdout
from collections import defaultdict
def le():
 return int(stdin.readline())
def lt():
 return list(map(int, stdin.readline().split()))
n=le()
lst=lt()
prev=defaultdict(lambda:0)
s=0
c=0
for i in range(n):
 s+=lst[i]
 if s==0:
  c+=1
 temp=[]
 if s in prev:
  c+=prev[s]
 prev[s]+=1
stdout.write(str(c))
