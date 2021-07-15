class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        events = []
        for i, (start, end) in enumerate(zip(startTime, endTime)):
            events.append((start, i + 1))
            events.append((end, -(i + 1)))
        
        best = 0
        for _, idx in sorted(events):
            if idx > 0:
                profit[idx - 1] += best
            else:
                best = max(best, profit[-idx - 1])
        return best

