import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 10**9+7
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    N, M = LI()
    G = collections.defaultdict(list)
    for _ in range(M):
        u, v, c = LI_()
        G[u].append((v, c))
        G[v].append((u, c))
    # print(G)
    ans = [-1] * N
    ans[0] = 1

    # 木に対して必ずよい書き込み方が存在するので、
    # DFSでMSTを辿ってよい書き込み方をすればよい
    def dfs(c, p):
        for n, l in G[c]:
            if ans[n] == -1:
                if ans[c] == l:
                    # 書き込む値がNを越えないようにする
                    if l < N - 1:
                        ans[n] = l + 1
                    else:
                        ans[n] = l - 1
                else:
                    ans[n] = l
                dfs(n, c)

    dfs(0, -1)

    for i in ans:
        print((i + 1))

def __starting_point():
    resolve()

__starting_point()
