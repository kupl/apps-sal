class Solution:
    def find(self, par, x):
        if par[x] == x:
            return x
        else:
            par[x] = self.find(par, par[x])
            return par[x]

    def merge(self, par, x, y):
        x = self.find(par, x)
        y = self.find(par, y)
        if x == y:
            return False
        par[x] = y
        return True

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        par = [i for i in range(len(points))]
        dis = lambda p1, p2: abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
        edges = []
        visited = set()
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                edges.append((dis(points[i], points[j]), i, j))
        edges.sort()
        r = 0
        for d, i, j in edges:
            if self.merge(par, i, j):
                r += d
        return r
