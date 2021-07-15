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
  n,k=geti()
  a=getl()
  occur=dd(int)
  ans=0
  temp=0
  temp_dict=dd(int)
  for i in a:
   occur[i]+=1
  for i in range(k):
   temp+=a[i]
   temp_dict[a[i]]+=1
  if (list(temp_dict.keys()))==(list(occur.keys())):
   ans=max(ans,temp)
  for i in range(k,n):
   temp-=a[i-k]
   temp_dict[a[i-k]]-=1
   if temp_dict[a[i-k]]==0:
    del temp_dict[a[i-k]]
   temp+=a[i]
   temp_dict[a[i]]+=1
   if (list(temp_dict.keys()))==(list(occur.keys())):
    ans=max(ans,temp)
  print(ans)


def __starting_point():
 solve()

__starting_point()
