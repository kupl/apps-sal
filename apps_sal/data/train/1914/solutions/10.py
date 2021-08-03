class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        diff = [cost[1] - cost[0] for cost in costs]
        heapq.heapify(diff)
        s = 0
        for cost in costs:
            s += cost[0]

        for i in range(len(costs) // 2):
            s += heapq.heappop(diff)

        return s
