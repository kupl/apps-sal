class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        result = set()
        intervals.sort(key=lambda x: (x[0], -x[1]))
        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                if j not in result and intervals[i][1] >= intervals[j][1]:
                    result.add(j)
        return len(intervals) - len(result)
