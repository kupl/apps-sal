from copy import deepcopy


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intind = []
        for i in range(0, len(intervals)):
            a = intervals[i][0]
            b = intervals[i][1]
            for j in range(i + 1, len(intervals)):
                c = intervals[j][0]
                d = intervals[j][1]
                if c <= a and b <= d:
                    intind.append(i)
                if a <= c and d <= b:
                    intind.append(j)
        return len(intervals) - len(set(intind))
