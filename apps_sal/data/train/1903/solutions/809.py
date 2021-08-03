class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        dist = {}
        edges = []
        for i in range(N):
            for j in range(i):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                dist[(i, j)] = d
                edges.append((d, i, j))
        edges.sort(reverse=True)
        uf = []
        ans = 0
        while len(edges) > 0:
            (d, a, b) = edges[-1]
            edges.pop()
            res = self.join(uf, a, b, N)
            if res == 2:
                break
            elif res == 1:
                ans += d
        return ans

    def join(self, ds, a, b, N):
        idx1 = -1
        for i in range(len(ds)):
            if a in ds[i]:
                idx1 = i
                break
        idx2 = -1
        for i in range(len(ds)):
            if b in ds[i]:
                idx2 = i
                break
        if idx1 == -1 and idx2 == -1:
            ds.append(set([a, b]))
        elif idx1 == idx2:
            return -1
        elif idx1 != -1 and idx2 != -1:
            u = ds[idx1].union(ds[idx2])
            ds[idx1] = 0
            ds[idx2] = 0
            ds.remove(0)
            ds.remove(0)
            ds.append(u)
        elif idx1 == -1:
            ds[idx2].add(a)
        elif idx2 == -1:
            ds[idx1].add(b)
        if len(ds) == 1 and ds[0] == 1:
            return 2
        return 1
