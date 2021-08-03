import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        L = len(points)
        if L <= 1:
            return 0

        todo = set(range(L))
        nex = 0
        h = []
        ans = 0
        while todo:
            todo.remove(nex)
            for i in todo:
                heapq.heappush(h, (distance(points[nex], points[i]), i))
            while h and h[0][1] not in todo:
                heapq.heappop(h)
            if not h:
                break
            cost, nex = heapq.heappop(h)
            ans += cost
        return ans
