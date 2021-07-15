import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import deque

MOD = 10 ** 9 + 7

N = int(input())
graph = [[] for _ in range(N+1)]
for i,x in enumerate(input().rstrip().split(),1):
    x = int(x)
    graph[i].append(x)
    graph[x].append(i)

# 各深さから来ている (0個、1個、2個以上) の分布を 確率 mod MODで持つ。

half = (MOD + 1) // 2

def merge(dp,dp1):
    L = len(dp1)
    for i in range(L):
        # 0個,1個,2個以上
        a,b,c = dp[i]
        d,e,f = dp1[i]
        a,b,c = a*d, a*e + b*d, a*f + b*e + b*f + c*d + c*e + c*f
        a %= MOD
        b %= MOD
        c %= MOD
        dp[i] = (a,b,c)
    return

def dfs(v,parent = None):
    dp = None
    L = 0
    for u in graph[v]:
        if u == parent:
            continue
        dp1 = dfs(u,v)
        if dp is None:
            dp = dp1
        else:
            if len(dp) < len(dp1):
                dp,dp1 = dp1,dp
            # 2個以上が入っているインデックス
            if L < len(dp1):
                L = len(dp1)
            merge(dp,dp1)
    if dp is None:
        dp = deque()
    else:
        # 2個以上あるときに、0個化する
        for i in range(L):
            a,b,c = dp[i]
            dp[i] = (a+c,b,0)
    dp.appendleft((half,half,0))
    return dp

dp = dfs(0)

answer = sum(b for a,b,c in dp)
answer *= pow(2,N+1,MOD)
answer %= MOD
print(answer)
