class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        for i in range(len(intervals)):
            if intervals[i] != None:
                for j in range(len(intervals)):
                    if i != j and intervals[j]:
                        if intervals[j][0] <= intervals[i][0] and intervals[i][1] <= intervals[j][1]:
                            intervals[i] = None
                            break
        for interval in intervals:
            if interval:
                count += 1
        return count
