class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        self.points = points
        n = len(points)
        edges = []
        for i in range(n - 1):
            for j in range(i + 1, n):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((d, i, j))
        edges.sort()
        self.comp = list(range(n))
        ans = 0
        e = 0
        for i in range(n - 1):
            while e < len(edges):
                d, i, j = edges[e]
                e += 1
                ii = self.find(i)
                jj = self.find(j)
                if ii != jj:
                    self.comp[ii] = jj
                    ans += d
                    break
        return ans

    def find(self, i):
        idx = []
        while self.comp[i] != i:
            idx.append(i)
            i = self.comp[i]
        for j in idx:
            self.comp[j] = i
        return i
