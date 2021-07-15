from sys import stdin, setrecursionlimit
import bisect, collections, copy, heapq, itertools, math, string
setrecursionlimit(10**8)

INF = float("inf")
MOD = 1000000007


def input():
    return stdin.readline().strip()

#unionfind
from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = collections.defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


def main():

    n, m = map(int, input().split())
    uf = UnionFind(n)
    adj = [[] for _ in range(n)]

    for _ in range(m):
        u, v, c = map(int, input().split())
        u -= 1
        v -= 1
        if uf.same(u, v): continue
        adj[u].append((v, c))    
        adj[v].append((u, c))
        uf.union(u, v)

    queue = collections.deque([0])
    ans = [-1]*n
    ans[0] = 1

    while queue:
        now = queue.popleft()
        pnum = ans[now]
        for edge in adj[now]:
            child = edge[0]
            enum = edge[1]
            if ans[child] != -1: continue
            queue.append(child)
            if pnum == enum:
                ans[child] = 1 if pnum != 1 else 2
            else:
                ans[child] = enum
    
    print(*ans, sep="\n")
















    return

def __starting_point():
    main()

__starting_point()
