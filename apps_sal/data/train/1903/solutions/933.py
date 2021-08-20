from heapq import heappush, heappop


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dists = [[float('inf')] * n for _ in range(n)]
        for (idx1, point1) in enumerate(points):
            for (idx2, point2) in enumerate(points):
                if idx1 != idx2:
                    manhattan = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
                    dists[idx1][idx2] = manhattan
                    dists[idx2][idx1] = manhattan
        res = 0
        nearest = [float('inf')] * n
        visited = set()
        h = [(0, 0)]
        while h and len(visited) < n:
            (last_dist, last_pt) = heappop(h)
            visited.add(last_pt)
            nearest[last_pt] = min(last_dist, nearest[last_pt])
            for (neigh_pt, neigh_dist) in enumerate(dists[last_pt]):
                if neigh_pt not in visited and neigh_dist < nearest[neigh_pt]:
                    heappush(h, (neigh_dist, neigh_pt))
        return sum(nearest)
