class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        cache = list(range(len(points)))

        def find(val):
            if cache[val] != val:
                cache[val] = find(cache[val])
            return cache[val]

        def union(x, y):
            cache[find(x)] = cache[find(y)]
        dists = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                dists.append((dist, i, j))
        dists.sort()
        ans = 0
        count = 0
        n = len(points)
        for (dist, a, b) in dists:
            if find(a) != find(b):
                count += 1
                ans += dist
                union(a, b)
            if count >= n - 1:
                break
        return ans
