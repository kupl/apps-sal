def manhattan(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        mstSet = set()
        (ans, n) = (0, len(points))
        queue = [(0, (0, 0))]
        while len(mstSet) < n:
            (weight, (u, v)) = heapq.heappop(queue)
            if v in mstSet:
                continue
            ans += weight
            mstSet.add(v)
            for j in range(n):
                if j not in mstSet and j != v:
                    heapq.heappush(queue, (manhattan(points[j], points[v]), (v, j)))
        return ans
