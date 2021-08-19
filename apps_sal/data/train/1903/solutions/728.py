class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def calc(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])
        #d = collections.defaultdict(dict)
        connections = []
        #seen = set()
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                if i != j:
                    #d[i][j]  = calc(points[i],points[j])
                    connections.append([i, j, calc(points[i], points[j])])

        connections.sort(key=lambda x: x[2])
        n = len(points)
        parent = [-1] * n
        size = [1] * n
        res = []

        def find(x):
            if parent[x] == -1:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            if px == py:
                return False
            if size[px] > size[py]:
                size[px] += size[py]
                parent[py] = px
            else:
                size[py] += size[px]
                parent[px] = py
            return True
        for s, d, w in connections:
            if union(s, d):
                res.append([s, d, w])
        ans = 0
        for a, b, c in res:
            ans += c

        # print(res)
        return ans
