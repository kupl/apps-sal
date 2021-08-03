class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 0

        dist_arr = []
        for i in range(n - 1):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                dist_arr.append((dist, i, j))
        heapq.heapify(dist_arr)

        root = [i for i in range(n)]

        def find(n):
            if root[n] != n:
                root[n] = find(root[n])
            return root[n]

        def union(x, y):
            s1 = find(x)
            s2 = find(y)
            if s1 != s2:
                root[s2] = root[s1]
                return 1
            return 0

        res = 0
        count = 0
        while count < n - 1:
            dist, x, y = heapq.heappop(dist_arr)
            if union(x, y) == 1:
                res += dist
                count += 1
        return res
