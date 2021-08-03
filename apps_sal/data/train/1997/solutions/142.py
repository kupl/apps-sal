class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        l = len(intervals)
        bad = []
        for i in range(l):
            if i not in bad:
                for j in range(i + 1, l):
                    if intervals[j][0] >= intervals[i][1]:
                        break
                    if j not in bad:
                        if intervals[i][0] == intervals[j][0]:
                            bad.append(i)
                            break
                        if intervals[j][1] <= intervals[i][1]:
                            bad.append(j)
        return l - len(bad)
