import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        total_cost = 0
        x1, y1 = points.pop()

        cost_heap = []
        heapq.heapify(cost_heap)
        for x2, y2 in points:
            heapq.heappush(cost_heap, [abs(x1 - x2) + abs(y1 - y2), x2, y2])

        while cost_heap:
            cost, x1, y1 = heapq.heappop(cost_heap)
            total_cost += cost
            for i, [cost, x2, y2] in enumerate(cost_heap):
                cost_heap[i][0] = min(cost, abs(x1 - x2) + abs(y1 - y2))
            cost_heap.sort()

        return total_cost
