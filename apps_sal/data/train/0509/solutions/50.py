import sys
from collections import deque
sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def LI2(): return list(map(int, sys.stdin.readline().rstrip()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def LS2(): return list(sys.stdin.readline().rstrip())


class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def same_check(self, x, y):
        return self.find(x) == self.find(y)

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        self.par[y] = x


N, M = MI()
Graph = [[] for _ in range(N + 1)]
UF = UnionFind(N)

for _ in range(M):
    u, v, c = MI()
    if not UF.same_check(u, v):
        UF.unite(u, v)
        Graph[u].append((v, c))
        Graph[v].append((u, c))

deq = deque([1])
ANS = [-1] * (N + 1)
ANS[1] = 1
while deq:
    i = deq.pop()
    for j, c in Graph[i]:
        if ANS[j] != -1:
            continue
        if ANS[i] != c:
            ANS[j] = c
        else:
            if c == 1:
                ANS[j] = 2
            else:
                ANS[j] = 1
        deq.append(j)

print(*ANS[1:], sep='\n')
