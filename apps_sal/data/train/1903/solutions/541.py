class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dsu = [i for i in range(n)]

        def get_root(id: int):
            dsu[id] = id if dsu[id] == id else get_root(dsu[id])
            return dsu[id]

        def unite(a: int, b: int) -> bool:
            a = get_root(a)
            b = get_root(b)
            if a == b:
                return False
            dsu[a] = b
            return True

        e = []
        for i in range(n):
            for j in range(i + 1, n):
                e.append([i, j, abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])])
        e.sort(key=lambda edge: edge[2])

        return sum([edge[2] for edge in e if unite(edge[0], edge[1])])
