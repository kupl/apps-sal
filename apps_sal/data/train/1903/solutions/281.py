class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        # lets give each edge a weight
        # an edge will be some point A to another point B
        # we will store the distances in a minheap
        # then we will perform union find to connect all points
        # using prim's algorithm - we choose the minimum from the current point we are at building out the MST
        if len(points) <= 1:
            return 0
        N = len(points)
        distances = [float('inf')] * N
        seen = set()
        ans = 0
        curr = 0
        for i in range(N - 1):
            x1, y1 = points[curr]
            seen.add(curr)
            for j in range(N):
                x2, y2 = points[j]
                if j in seen:
                    continue
                distances[j] = min(abs(x1 - x2) + abs(y1 - y2), distances[j])
            delta, curr = min((d, j) for j, d in enumerate(distances))
            distances[curr] = float('inf')
            ans += delta
        return ans
