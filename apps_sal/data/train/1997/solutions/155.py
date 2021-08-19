class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        covered = []
        for i in range(len(intervals)):
            if i in covered:
                continue
            i1 = intervals[i]
            for j in range(i + 1, len(intervals)):
                if j in covered:
                    continue
                i2 = intervals[j]
                if i1[0] <= i2[0] and i1[1] >= i2[1]:
                    covered.append(j)
                elif i1[0] >= i2[0] and i1[1] <= i2[1]:
                    covered.append(i)
                    break
        return len(intervals) - len(covered)
