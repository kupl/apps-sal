class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def dist(points):
            (x, y) = points
            return abs(x[0] - y[0]) + abs(x[1] - y[1])
        new_points = []
        for first in points:
            for second in points:
                if first != second:
                    new_points.append((first, second))
        new_points.sort(key=lambda x: dist(x))

        def find(x):
            if x not in parent:
                parent[x] = x
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            (nx, ny) = (find(x), find(y))
            if nx == ny:
                return False
            if rank[nx] > rank[ny]:
                parent[ny] = nx
                size[nx] += size[ny]
            elif rank[nx] < rank[ny]:
                parent[nx] = ny
                size[ny] += size[nx]
            else:
                parent[nx] = ny
                size[ny] += size[nx]
                rank[ny] += 1
            return True
        parent = {}
        rank = defaultdict(int)
        size = defaultdict(lambda: 1)
        res = 0
        for (x, y) in new_points:
            x = tuple(x)
            y = tuple(y)
            if union(x, y):
                res += dist((x, y))
            if size[x] == len(points):
                return res
        return res
