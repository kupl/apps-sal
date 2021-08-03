class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        removed = []
        for i, interval in enumerate(intervals):
            for i2 in range(i, len(intervals)):
                interval2 = intervals[i2]
                if i in removed:
                    break
                if i == i2 or i2 in removed:
                    continue
                if interval[0] >= interval2[0] and interval[1] <= interval2[1] and i not in removed:
                    removed += [i]
                if interval[0] <= interval2[0] and interval[1] >= interval2[1] and i2 not in removed:
                    removed += [i2]

        return len(intervals) - len(removed)
