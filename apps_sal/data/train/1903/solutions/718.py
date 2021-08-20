class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        connections = []
        self.father = {}
        self.size = n
        for i in range(n):
            self.father[points[i][0], points[i][1]] = (points[i][0], points[i][1])
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                p1 = (points[i][0], points[i][1])
                p2 = (points[j][0], points[j][1])
                connections.append((p1, p2, dist))
        connections = sorted(connections, key=lambda x: x[2])
        res = 0

        def union(a, b):
            root_a = find(a)
            root_b = find(b)
            if root_a != root_b:
                self.father[root_a] = root_b
                self.size -= 1
                return True
            else:
                return False

        def find(node):
            path = []
            while node != self.father[node]:
                path.append(node)
                node = self.father[node]
            for child in path:
                self.father[child] = node
            return node
        for c in connections:
            if union(c[0], c[1]):
                res += c[2]
                if self.size == 0:
                    return res
        return res
