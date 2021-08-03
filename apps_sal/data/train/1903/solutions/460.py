class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # dikstra algo
        if len(points) == 0:
            return 0
        heap = []
        for i in range(1, len(points)):
            heapq.heappush(heap, (abs(points[i][0] - points[0][0]) + abs(points[i][1] - points[0][1]), i))
        ret = 0
        while heap:
            cost, e_pop = heapq.heappop(heap)
            ret += cost
            heap_new = []
            for cost_old, e in heap:
                heapq.heappush(heap_new, (min(cost_old, abs(points[e][0] - points[e_pop][0]) + abs(points[e][1] - points[e_pop][1])), e))
            heap = heap_new
        return ret
