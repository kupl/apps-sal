class Solution:

    def jobScheduling(self, startTime, endTime, profit):
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[0])
        heap = []
        total = 0
        for (s, e, p) in jobs:
            while heap and heap[0][0] <= s:
                (end, profit) = heappop(heap)
                total = max(total, profit)
            heappush(heap, (e, p + total))
        while heap:
            (end, profit) = heappop(heap)
            total = max(total, profit)
        return total
