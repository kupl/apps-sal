class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        discarded = [False] * len(intervals)
        for i in range(len(intervals)):
            for j in range(len(intervals)):
                if i == j:
                    continue
                if discarded[j]:
                    continue
                if intervals[j][0] >= intervals[i][0] and intervals[j][1] <= intervals[i][1]:
                    discarded[j] = True
        kount = 0
        for i in range(len(intervals)):
            if not discarded[i]:
                kount = kount + 1
        return kount
