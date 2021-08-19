import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


class UnionFind:

    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        """xの親を返す"""
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        """yをxの根に繋ぐ（マージテク有）"""
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            (x, y) = (y, x)
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        """xとyが同じ連結成分か判別する"""
        return self.find(x) == self.find(y)

    def size(self, x):
        """xの連結成分の大きさを返す"""
        return -self.parents[self.find(x)]

    def kruskal(self, edge):
        """
        :param edge: edge = [(コスト, 頂点1, 頂点2),...]の形で重み付き隣接リストを渡して下さい
        :return: 最小全域木のコストの和
        """
        edge.sort()
        cost_sum = 0
        for (cost, node1, node2) in edge:
            if not self.same(node1, node2):
                cost_sum += cost
                self.union(node1, node2)
        return cost_sum


def resolve():

    def dfs(v):
        for (d, u) in edge[v]:
            if uf.same(v, u):
                continue
            uf.union(u, v)
            if res[v] != d:
                res[u] = d
            else:
                for i in range(1, n + 1):
                    if i != d:
                        res[u] = i
                        break
            dfs(u)
    (n, m) = map(int, input().split())
    edge = [[] for _ in range(n)]
    for _ in range(m):
        (u, v, c) = map(int, input().split())
        edge[u - 1].append([c, v - 1])
        edge[v - 1].append([c, u - 1])
    uf = UnionFind(n)
    res = [0] * n
    res[0] = 1
    dfs(0)
    print(*res, sep='\n')


def __starting_point():
    resolve()


__starting_point()
