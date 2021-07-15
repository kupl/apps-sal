#from collections import deque,defaultdict
printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 10**18
#R = 10**9 + 7
R = 998244353

def ddprint(x):
  if DBG:
    print(x)

n,k = inm()
dp = [[0]*(n+1) for i in range(n+1)]
dp[0][0] = 1
for i in range(1,n+1):
    for j in range(i,0,-1):
        dp[i][j]=(dp[i-1][j-1]+(dp[i][2*j] if 2*j<=i else 0))%R
print(dp[n][k])

