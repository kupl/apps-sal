class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: (x[0], -x[1]))
        ans = len(intervals)
        i = 0
        while i < len(intervals):
            for j in range(i):
                if intervals[j][0] <= intervals[i][0] and intervals[j][1] >= intervals[i][1]:
                    ans -= 1
                    break
            i += 1
        return ans
