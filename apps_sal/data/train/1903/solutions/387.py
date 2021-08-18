class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        connections = []

        for i, p in enumerate(points):
            for j in range(i + 1, len(points)):
                connections.append((i, j, abs(p[0] - points[j][0]) + abs(p[1] - points[j][1])))

        connections.sort(key=itemgetter(2))
        parent = list(range(len(points)))
        size = [1] * len(points)

        def find(x):
            if x == parent[x]:
                return x

            parent[x] = find(parent[x])
            return parent[x]

        total_distance = 0
        for u, v, c in connections:
            p_u = find(u)
            p_v = find(v)

            if p_u == p_v:
                continue

            total_distance += c
            if size[u] < size[v]:
                size[v] += size[u]
                parent[p_u] = p_v
            else:
                size[u] += size[v]
                parent[p_v] = p_u

        return total_distance
