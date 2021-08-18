class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        covered = 0
        same = 0
        for i in range(len(intervals)):
            for j in range(len(intervals)):
                if intervals[i][0] == intervals[j][0] and intervals[j][1] == intervals[i][1]:
                    continue
                elif intervals[i][0] >= intervals[j][0] and intervals[j][1] >= intervals[i][1]:
                    covered += 1
                    break
        return len(intervals) - covered
