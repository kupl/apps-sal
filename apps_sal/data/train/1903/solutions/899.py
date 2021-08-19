class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        data = [i for i in range(len(points))]
        pq = []
        res = 0

        def helper(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        def find(x):
            if x != data[x]:
                data[x] = find(data[x])
            return data[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return False
            data[root_x] = root_y
            return True
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                heapq.heappush(pq, (helper(points[i], points[j]), i, j))
        res = 0
        while pq:
            (cost, p1, p2) = heapq.heappop(pq)
            if union(p1, p2):
                res += cost
        return res
