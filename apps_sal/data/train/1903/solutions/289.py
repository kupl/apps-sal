class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
        pq = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                temp = abs(points[j][1] - points[i][1]) + abs(points[j][0] - points[i][0])
                heapq.heappush(pq, (temp, (i, j)))
        root = list(range(len(points)))

        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]

        def union(x, y):
            (rx, ry) = (find(x), find(y))
            if rx == ry:
                return False
            root[rx] = root[ry]
            return True
        res = 0
        conn = 0
        while conn < len(points) - 1:
            (cost, xy) = heapq.heappop(pq)
            (x, y) = xy
            if union(x, y):
                res += cost
                conn += 1
        return res
