import sys
from bisect import bisect_left
sys.setrecursionlimit(10**7)
def input():return sys.stdin.readline().strip()

def main():
    N = int(input())
    A = tuple(map(int, input().split()))

    to = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        to[u].append(v)
        to[v].append(u)
    
    ans = [0] * N
    dp = []
    def dfs(now, pre):
        a = A[now]
        idx = bisect_left(dp, a)

        if idx == len(dp):
            old = -1
            dp.append(a)
        else:
            old = dp[idx]
            dp[idx] = a
        
        ans[now] = len(dp)

        
        for nv in to[now]:
            if nv != pre:
                dfs(nv, now)
        

        if old == -1:
            dp.pop()
        else:
            dp[idx] = old

    
    dfs(0, -1)

    print(*ans, sep="\n")
        

def __starting_point():
    main()
__starting_point()
