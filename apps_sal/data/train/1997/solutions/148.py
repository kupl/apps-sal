class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        notCovered = len(intervals)
        covered = len(intervals) * [False]

        intervals.sort(key=lambda x: (x[0], -x[1]))

        for i in range(len(intervals)):
            if not covered[i]:
                for j in range(i + 1, len(intervals)):
                    if not covered[j]:
                        firstIntervalEnd = intervals[i][1]
                        secondIntervalEnd = intervals[j][1]
                        if secondIntervalEnd <= firstIntervalEnd:
                            covered[j] = True
                            notCovered -= 1

        return notCovered
