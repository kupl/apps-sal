class Solution:
    # Time: O(n^2)
    # Space: O(n)
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 0
        res, curr = 0, 0
        distances = [float('inf') for _ in range(n)]
        explored = set()
        
        for i in range(n - 1):
            x0, y0 = points[curr]
            explored.add(curr)
            for j, (x, y) in enumerate(points):
                if j in explored:
                    continue
                distances[j] = min(distances[j], abs(x0 - x) + abs(y0 - y))
                
            delta, curr = min((d, j) for j, d in enumerate(distances))
            res += delta
            distances[curr] = float('inf')
            
        return res         
