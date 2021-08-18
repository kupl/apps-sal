from collections import defaultdict
dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]


class DSU:
    def __init__(self, n):
        self.n = n
        self.parent = [x for x in range(n)]
        self.rank = [0 for x in range(n)]
        self.land = [False for x in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, s, t):
        sp, tp = self.find(s), self.find(t)
        if sp == tp:
            return
        if self.rank[sp] > self.rank[tp]:
            self.parent[tp] = sp
        elif self.rank[sp] < self.rank[tp]:
            self.parent[sp] = tp
        else:
            self.parent[sp] = tp
            self.rank[tp] += 1


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        net = DSU(m * n)
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    continue
                net.land[r * n + c] = True
                for d in dirs:
                    nr, nc = r + d[0], c + d[1]
                    if not (0 <= nr < m) or not (0 <= nc < n):
                        continue
                    elif grid[nr][nc] == 1:
                        continue
                    net.union(r * n + c, nr * n + nc)
        ihm = defaultdict(list)
        for i in range(m * n):
            p = net.find(i)
            if net.land[p]:
                ihm[p].append((i // n, i % n))
        islands = list(ihm.values())
        ret = 0
        for pl in islands:
            isClosed = True
            for p in pl:
                r, c = p[0], p[1]
                if r == m - 1 or c == n - 1 or r == 0 or c == 0:
                    isClosed = False
                    break
            if isClosed:
                ret += 1
        return ret
