class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 0
        vis = set()
        points = list(map(tuple, points))
        q = [(0, points[0])]
        res = 0

        def get_dist(pointa, pointb):
            return abs(pointa[0] - pointb[0]) + abs(pointa[1] - pointb[1])
        while q:
            top, curr_pt = heappop(q)
            if curr_pt in vis:
                continue
            vis.add(curr_pt)
            res += top
            for point in set(points) - vis:
                heappush(q, (get_dist(curr_pt, point), point))

        return res
