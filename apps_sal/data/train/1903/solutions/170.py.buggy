class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if len(points) == 1: 
            return 0
        ans = curr = 0
        d = [float(\"inf\")] * n
        v = set()
        for _ in range(n-1):
            x0, y0 = points[curr]
            v.add(curr)
            for j, (x, y) in enumerate(points):
                if j not in v:
                    d[j] = min(d[j], abs(x-x0) + abs(y-y0)) 
            delta, curr = min((v, j) for j, v in enumerate(d)) 
            d[curr] = float(\"inf\")
            ans += delta
        return ans
