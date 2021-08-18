class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        removed = []
        for i in range(len(intervals) - 1):
            for j in range(i + 1, len(intervals)):
                if i in removed:
                    break
                if j in removed:
                    continue
                i_start, i_end = intervals[i]
                j_start, j_end = intervals[j]
                if i_start <= j_start and i_end >= j_end:
                    removed.append(j)
                elif i_start >= j_start and i_end <= j_end:
                    removed.append(i)
        return len(intervals) - len(removed)
