from queue import PriorityQueue


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        q = PriorityQueue()
        x0, y0 = points[0]
        for x, y in points[1:]:
            q.put([abs(x - x0) + abs(y - y0), x, y])
        cost = 0
        to_process = set([(x, y) for x, y in points[1:]])
        while len(to_process) > 0:
            d, x, y = q.get()
            if (x, y) not in to_process:
                continue
            to_process.remove((x, y))
            cost += d
            for nx, ny in to_process:
                q.put([abs(x - nx) + abs(y - ny), nx, ny])
        return cost
