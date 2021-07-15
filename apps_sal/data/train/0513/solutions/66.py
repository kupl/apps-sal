import sys
sys.setrecursionlimit(100000000)
from  bisect import bisect_left
input = sys.stdin.readline
INF = 1 << 30

MAXN = 200005
G = [[] for _ in range(MAXN)]
dp = [INF] * MAXN
stack = []
ans = [None] * MAXN
def dfs(v,A,p = -1):
    idx = bisect_left(dp,A[v])
    stack.append((idx,dp[idx]))
    dp[idx] = A[v]
    ans[v] = bisect_left(dp,INF)
    for e in G[v]:
        if e == p:
            continue
        dfs(e,A,v)
    idx,p = stack.pop()
    dp[idx] = p

def main():
    N = int(input())
    A = list(map(int,input().split()))
    for _ in range(N - 1):
        a,b = list(map(int,input().split()))
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)
    dfs(0,A)
    print(('\n'.join(map(str,ans[:N]))))
def __starting_point():
    main()
    

    
    

__starting_point()
