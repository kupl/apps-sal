import sys
import math
import bisect
from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd
from bisect import bisect_left as bl,bisect_right as br

sys.setrecursionlimit(100000000)

ii =lambda: int(input())
si =lambda: input()
jn =lambda x,l: x.join(map(str,l))
sl =lambda: list(map(str,input().strip()))
mi =lambda: list(map(int,input().split()))
mif =lambda: list(map(float,input().split()))
lii =lambda: list(map(int,input().split()))

ceil =lambda x: int(x) if(x==int(x)) else int(x)+1
ceildiv=lambda x,d: x//d if(x%d==0) else x//d+1

flush =lambda: stdout.flush()
stdstr =lambda: stdin.readline()
stdint =lambda: int(stdin.readline())
stdpr =lambda x: stdout.write(str(x))

mod=1000000007
def sol(s):  
 dp = [0] * (len(s) + 2)
 dp[0] = 1
  
 for i in range(len(s)):
  if int(s[i]) != 0:
   dp[i+1] += dp[i]
   
  if int(s[i:i+2]) >= 10 and int(s[i:i+2]) <= 26:
   dp[i+2] += dp[i]
  
 return dp[len(s)] 
 


#main code
for _ in range(ii()):
 s=si()
 ans=sol(s)
 print(ans%mod)

