def manhattan(coor1, coor2):
        return abs(coor1[0] - coor2[0]) + abs(coor1[1] - coor2[1])

def find(C, u):
    if C[u] != u:
        C[u] = find(C, C[u])
    return C[u]

def naive_union(C, u, v):
    u, v = find(C, u), find(C, v)
    C[u] = v

class Solution(object):
    def minCostConnectPoints(self, points):
        \"\"\"
        :type points: List[List[int]]
        :rtype: int
        \"\"\"
        edges = [(manhattan(points[u], points[v]), u, v) for u in range(len(points) - 1) for v in range(u + 1, len(points))]
        edges = sorted(edges)
        C = {u: u for u in range(len(points))}
        res = 0
        for dis, u, v in edges:
            if find(C, u) != find(C, v):
                naive_union(C, u, v)
                res += dis
        return res
