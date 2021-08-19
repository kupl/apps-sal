class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        for i in range(len(intervals) - 1):
            for j in range(len(intervals) - i - 1):
                if intervals[j][0] > intervals[j + 1][0]:
                    (intervals[j], intervals[j + 1]) = (intervals[j + 1], intervals[j])
        i = 0
        while True:
            while intervals[i][1] >= intervals[i + 1][1]:
                intervals.pop(i + 1)
                if i + 1 > len(intervals) - 1:
                    break
            if i + 1 > len(intervals) - 1:
                break
            if intervals[i][0] == intervals[i + 1][0]:
                intervals.pop(i)
                if i + 1 > len(intervals) - 1:
                    break
                else:
                    continue
            if i + 1 == len(intervals) - 1:
                break
            i += 1
        return len(intervals)
