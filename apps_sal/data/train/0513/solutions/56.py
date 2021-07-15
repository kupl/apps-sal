from collections import deque
from bisect import bisect_left
import sys
def input():return sys.stdin.readline().strip()

def main():
    N = int(input())
    A = tuple(map(int, input().split()))

    to = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        to[a].append(b)
        to[b].append(a)
    
    # bfs
    INF = 10 ** 18
    dp = [INF] * N
    ans = [0] * N

    def dfs(s):
        stack = deque()
        pop = stack.pop
        push = stack.append

        push((s, -1, None))

        while stack:
            now, pre, old = pop()

            # 復元
            if now == -1:
                dp[pre] = old
                continue
            
            a = A[now]
            idx = bisect_left(dp, a)
            old = dp[idx]
            dp[idx] = a

            ans_idx = bisect_left(dp, INF)
            ans[now] = ans_idx

            # 復元用 頂点
            # (フラグ, 変更したidx, 前の値)
            push((-1, idx, old))
            
            for nv in to[now]:
                if nv != pre:
                    push((nv, now, None))
    
    dfs(0)
    print(*ans, sep="\n")

def __starting_point():
    main()
__starting_point()
