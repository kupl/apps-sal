class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
        root = {}
        for point in points:
            root[point[0], point[1]] = (point[0], point[1])

        def find(i):
            if i != root[i]:
                root[i] = find(root[i])
            return root[i]

        def union(a, b):
            (a, b) = (find(a), find(b))
            if a == b:
                return 0
            root[a] = b
            return 1
        num = len(points)
        edge_count = 0
        distances = []
        for i in range(num):
            for j in range(i + 1, num):
                distances.append((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), (points[i], points[j])))
                j += 1
        distances.sort(key=lambda x: x[0])
        ans = 0
        for d in distances:
            a = d[1][0]
            b = d[1][1]
            a_t = tuple(a)
            b_t = tuple(b)
            if find(a_t) != find(b_t):
                edge_count += 1
                ans += d[0]
                union(a_t, b_t)
                if edge_count == num - 1:
                    return ans
        return -1
