from heapq import *


class Solution:

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        heap = []
        max_profit = 0
        for (start, end, p) in jobs:
            while heap and heap[0][0] <= start:
                max_profit = max(max_profit, heappop(heap)[1])
            heappush(heap, (end, max_profit + p))
        for (_, p) in heap:
            max_profit = max(max_profit, p)
        return max_profit
