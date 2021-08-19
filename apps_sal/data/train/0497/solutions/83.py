from heapq import *


class Solution:

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        heap = []
        max_profit = 0
        for job in jobs:
            while heap and heap[0][0] <= job[0]:
                max_profit = max(max_profit, heappop(heap)[1])
            heappush(heap, (job[1], max_profit + job[2]))
        for item in heap:
            max_profit = max(max_profit, item[1])
        return max_profit
