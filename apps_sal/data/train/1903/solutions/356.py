class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        distances = []
        n = len(points)
        for i in range(n - 1):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                distances.append([(i, j), dist])
        distances.sort(key=lambda x: x[1])
        # print(distances)
        parent = [i for i in range(n)]
        size = [1 for _ in range(n)]

        def find(x):
            if parent[x] == x:
                return x
            else:
                return find(parent[x])

        def union(px, py):
            # px, py = find(x), find(y)
            # if px != py:
            if size[px] < size[py]:
                px, py = py, px
            parent[py] = px
            size[px] += size[py]
        count = 0
        ans = 0
        for (x, y), dist in distances:
            px, py = find(x), find(y)
            if px != py:
                union(px, py)
                count += 1
                ans += dist
                if count == n - 1:
                    break
        return ans
