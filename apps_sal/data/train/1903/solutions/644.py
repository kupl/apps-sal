# mst
# sort edge->union find
# choose min that is not connected
def distance(u, v):
    return abs(u[0] - v[0]) + abs(u[1] - v[1])


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        distances = []
        n = len(points)
        mini = 0
        parent = [i for i in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                u, v = points[i], points[j]
                dis = distance(u, v)
                distances.append((dis, i, j))
        distances.sort()  # distance, u, v

        def find(i):
            while i != parent[i]:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i

        def union(i, j):
            a, b = find(i), find(j)
            if a == b:
                return False
            else:
                parent[a] = b
                return True

        for cost, i, j in distances:
            if union(i, j):
                mini += cost
            else:
                mini += 0

        return mini
