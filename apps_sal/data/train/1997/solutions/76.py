class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        counter = 0
        l = len(intervals)
        for i in range(l):
            for j in range(l):
                if i != j:
                    if intervals[j][0] <= intervals[i][0] and intervals[i][1] <= intervals[j][1]:
                        counter += 1
                        break
        return l - counter
