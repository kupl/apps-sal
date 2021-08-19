class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def dis(p1, p2):
            (x1, y1) = p1
            (x2, y2) = p2
            return abs(x1 - x2) + abs(y1 - y2)
        size = len(points)
        cost = 0
        idx = list(range(size))

        def find(x):
            if x != idx[x]:
                idx[x] = find(idx[x])
            return idx[x]

        def union(x, y):
            (xx, yy) = (find(x), find(y))
            if xx == yy:
                return False
            idx[xx] = yy
            return True
        edges = []
        for i in range(size):
            for j in range(i + 1, size):
                distance = dis(points[i], points[j])
                edges.append((distance, i, j))
        edges.sort()
        for (dis, x, y) in edges:
            if union(x, y):
                cost += dis
                size -= 1
                if size == 1:
                    return cost
        return cost
