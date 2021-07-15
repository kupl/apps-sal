class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dist = {}
        n = len(points)
        queue = []
        for i in range(n):
            x = points[i]
            for j in range(i + 1, n):
                y = points[j]
                heapq.heappush(queue, (abs(x[0] - y[0]) + abs(x[1] - y[1]), i, j))
                
        parents = list(range(n))
        rank = [1] * n
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            if rank[px] < rank[py]:
                px, py = py, px
            parents[py] = px
            rank[px] += rank[px] == rank[py]
            return True
                
        result = 0
        for _ in range(n - 1):
            while True:
                dist, i, j = heapq.heappop(queue)
                if union(i, j):
                    result += dist
                    break
        return result
            

