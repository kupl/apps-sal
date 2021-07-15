class Solution:
    def find(self, roots, x):
        if x == roots[x]:
            return x
        return self.find(roots, roots[x])
    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                d = abs(x1 - x2) + abs(y1 - y2)
                edges.append((d, i, j))
        edges.sort()
        roots = list(range(n))
        ranks = [0] * n
        count = 0
        res = 0
        for d, x, y in edges:
            rx = self.find(roots, x)
            ry = self.find(roots, y)
            if rx != ry:                
                if ranks[rx] > ranks[ry]:
                    roots[ry] = rx
                elif ranks[rx] < ranks[ry]:
                    roots[rx] = ry
                else:
                    roots[ry] = rx
                    ranks[rx] += 1
                count += 1
                res += d
                if count == n - 1:
                    return res
        
        return res
