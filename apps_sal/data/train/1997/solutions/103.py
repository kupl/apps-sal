class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        valid = []
        for (index, (i, j)) in enumerate(intervals):
            for (ii, jj) in intervals[:index] + intervals[index + 1:]:
                if ii <= i and jj >= j:
                    break
            else:
                valid.append([i, j])
        print(valid)
        return len(valid)
