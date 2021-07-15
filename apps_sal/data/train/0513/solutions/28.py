import sys
from bisect import bisect_left
def main():
    sys.setrecursionlimit(202020)
    N = int(input())
    A = [0] + list(map(int, input().split()))
    G = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u, v = list(map(int, input().split()))
        G[u].append(v)
        G[v].append(u)
    L = [A[1]]
    Ans = [0] * (N+1)
    def dfs(v):
        Ans[v] = len(L)
        for u in G[v]:
            G[u].remove(v)
            Au = A[u]
            if Au > L[-1]:
                L.append(Au)
                dfs(u)
                del L[-1]
            else:
                idx = bisect_left(L, Au)
                old = L[idx]
                L[idx] = Au
                dfs(u)
                L[idx] = old
    dfs(1)
    print(("\n".join(map(str, Ans[1:]))))

main()

