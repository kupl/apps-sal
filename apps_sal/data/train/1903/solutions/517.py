def dist(p1, p2):
    return int(abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]))


def find(x, uf):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x], uf)
    return uf[x]


def union(x, y, uf):
    xx = find(x, uf)
    yy = find(y, uf)
    if xx == yy:
        return False
    uf[xx] = yy
    return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                edges.append((dist(points[i], points[j]), i, j))
        edges.sort()
        uf = list(range(n))
        ans = 0
        for e in edges:
            if union(e[1], e[2], uf):
                ans += e[0]
        return ans
