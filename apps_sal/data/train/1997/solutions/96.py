class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        deleted = set()
        for idx, interval in enumerate(intervals):
            if str(interval) in deleted:
                continue
            for other in intervals[idx + 1:]:
                if interval[0] <= other[0] and interval[1] >= other[1]:
                    deleted.add(str(other))
                elif interval[0] >= other[0] and interval[1] <= other[1]:
                    deleted.add(str(interval))
        return len(intervals) - len(deleted)
