class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        non_covered_intervals = []
        covered_intervals = set()
        for i in range(len(intervals)):
            for j in range(len(intervals)):
                if j == i:
                    continue
                if tuple(intervals[j]) in covered_intervals:
                    continue
                if intervals[i][0] >= intervals[j][0] and intervals[i][1] <= intervals[j][1]:
                    covered_intervals.add(tuple(intervals[i]))
                    break
            else:
                non_covered_intervals.append(intervals[i])
        return len(non_covered_intervals)
