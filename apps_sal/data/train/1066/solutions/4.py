from sys import stdin, stdout
input = stdin.readline
from collections import defaultdict as dd
import math
def geti(): return list(map(int, input().strip().split()))
def getl(): return list(map(int, input().strip().split()))
def gets(): return input()
def geta(): return int(input())
def print_s(s): stdout.write(s+'\n')

def solve():
 for _ in range(geta()):
  n=geta()
  num=list(map(int,list(str(n))))
  # print(num)
  index=-1
  for i in range(len(num)-1):
   if num[i]>num[i+1]:
    index=i
    break
  else:
   print(n)
   continue
  if index!=-1:
   fake=num[index]
   for i in range(index,-1,-1):
    if num[i]==fake:
     num[i]-=1
     last=i
   for i in range(last+1,len(num)):
    num[i]=9
   ans=0
   for i in num:
    ans*=10
    ans+=i
   print(ans)


def __starting_point():
 solve()

__starting_point()
