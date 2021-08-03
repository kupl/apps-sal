class Solution:

    def covered(self, interval_1, interval_2):
        return interval_2[0] <= interval_1[0] and interval_2[1] >= interval_1[1]

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        i = 0
        while (i < len(intervals)):
            j = 0
            while (j < len(intervals)):
                print((len(intervals), i, j))
                if j == i or intervals[j][0] > intervals[i][0]:
                    j += 1
                    continue
                elif self.covered(intervals[i], intervals[j]):
                    intervals.pop(i)
                    i -= 1
                    break
                else:
                    j += 1
                    continue
            i += 1

        return len(intervals)
