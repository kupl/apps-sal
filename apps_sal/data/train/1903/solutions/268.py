import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        if len(points) == 1:
            return 0

        def manhattan(x1, x2):
            return abs(x1[0] - x2[0]) + abs(x1[1] - x2[1])

        total_cost = 0
        first_chosen = points.pop()
        cost_heap = []

        for point in points:
            heapq.heappush(cost_heap, [manhattan(point, first_chosen), point])

        while cost_heap:
            cost, new_point = heapq.heappop(cost_heap)
            total_cost += cost
            for i, [cost, point] in enumerate(cost_heap):
                cost_heap[i][0] = min(cost, manhattan(point, new_point))
            cost_heap.sort()

        return total_cost
