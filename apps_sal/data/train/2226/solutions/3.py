
from sys import stdin
import sys
import heapq

def bitadd(a,w,bit):
 
    x = a+1
    while x <= (len(bit)-1):
        bit[x] += w
        x += x & (-1 * x)
 
def bitsum(a,bit):
 
    ret = 0
    x = a+1
    while x > 0:
        ret += bit[x]
        x -= x & (-1 * x)
    return ret

n = int(stdin.readline())
s = stdin.readline()[:-1]

bit = [0] * (n+10)
dp = [0] * (n+10)

y = 0
ans = 0
for i in range(n):

    if s[i] == "0":
        while y > 0:
            dp[y] += 1
            bitadd(y,y,bit)
            y -= 1
        dp[0] += 1
    else:
        bitadd(y,-1*dp[y]*y,bit)
        bitadd(y+1,-1*dp[y+1]*(y+1),bit)
        dp[y+1] += dp[y]
        dp[y] = 0
        y += 1
        bitadd(y,dp[y]*y,bit)
        
    now = bitsum(i,bit) + (1+y)*y//2
    #print (bitsum(i,bit),(1+y)*y//2,dp)
    ans += now
    
print (ans)
