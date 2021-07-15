class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        cnt = len(points)
        dist = []
        connected = [False] * cnt
        
        for i in range(cnt):
            for j in range(i):
                p1, p2 = points[i], points[j]
                tmp_d = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                dist.append([(i, j), tmp_d])
        
        res = 0
        dist = sorted(dist, key = lambda d: d[1])
        
        parent = [i for i in range(cnt)]
        
        def findp(x):
            if parent[x] != x: return findp(parent[x])
            return x
        
        def combine(x, y):
            px, py = findp(x), findp(y)
            parent[px] = py
            
        for d in dist:
            if findp(d[0][0]) != findp(d[0][1]):
                combine(d[0][0], d[0][1])
                res += d[1]
        
        return res
        

