class Solution:

    def removeCoveredIntervals(self, interval: List[List[int]]) -> int:
        c = len(interval)
        for i in range(len(interval)):
            for j in range(len(interval)):
                if i != j and interval[j][0] >= 0 and (interval[j][1] >= 0):
                    if interval[i][0] <= interval[j][0] and interval[i][1] >= interval[j][1]:
                        c -= 1
                        interval[j] = [-1, -1]
        return c
