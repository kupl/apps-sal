class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0

        def get_dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        (seen, res) = (set([0]), 0)
        heap = [(get_dist(points[0], p2), i + 1) for (i, p2) in enumerate(points[1:])]
        heapq.heapify(heap)
        while heap:
            (dist, index) = heapq.heappop(heap)
            if index in seen:
                continue
            seen.add(index)
            res += dist
            for i in range(len(points)):
                if i != index and i not in seen:
                    heapq.heappush(heap, (get_dist(points[i], points[index]), i))
        return res
