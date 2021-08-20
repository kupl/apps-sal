class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        N = len(intervals)
        intervals.sort(key=lambda x: x[0])
        count = 0
        covered = set()
        for i in range(N):
            for j in range(N):
                if i != j and j not in covered:
                    min_x = min(intervals[i][0], intervals[j][0])
                    max_y = max(intervals[i][1], intervals[j][1])
                    if intervals[i] == [min_x, max_y]:
                        covered.add(j)
                        count += 1
        return N - count
