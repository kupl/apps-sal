import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        total_cost = 0
        # any initial point can be chosen
        x1, y1 = points.pop() 
        # then make a heap sorted by distance to that point
        
        cost_heap = []
        heapq.heapify(cost_heap)
        for x2, y2 in points:
            heapq.heappush(cost_heap, [abs(x1-x2) + abs(y1-y2), x2, y2])
        
        # pop off the points with the lowest distance
        # then see if any of the remaining points are closer to that new point than
        # the previous points had been, and update the heap
        while cost_heap:
            cost, x1, y1 = heapq.heappop(cost_heap)
            total_cost += cost
            for i, [cost, x2, y2] in enumerate(cost_heap):
                cost_heap[i][0] = min(cost, abs(x1-x2) + abs(y1-y2))
            heapq.heapify(cost_heap)
            
        return total_cost
