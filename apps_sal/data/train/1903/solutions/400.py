class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        uf = {}
        n = len(points)
        rank = [1] * n
        
        def find(x):
            uf.setdefault(x, x)
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                if rank[px] > rank[py]:
                    px, py = py, px
                rank[py] += rank[px]
                uf[px] = py
                return rank[py] == n
            return False
        
        hp = [(abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j) for i in range(n) for j in range(i + 1, n)]
        heapq.heapify(hp)
        ans = 0
        
        while hp:
            d, i, j = heapq.heappop(hp)
            if find(i) != find(j):
                ans += d
                if union(i, j):
                    break
                
        return ans
