class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 0
        dic = {}
        for i in range(n - 1):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                dic[(i, j)] = dist

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

        dic_sorted = sorted(list(dic.items()), key=lambda x: x[1])
        res = 0
        count = 0
        for item in dic_sorted:
            x, y = item[0]
            dist = item[1]
            if union(x, y) == 1:
                res += dist
                count += 1
            if count == n - 1:
                return res
        # return res
