class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        covered = set()
        for i in range(len(intervals) - 1):
            a1, b1 = intervals[i]
            for j in range(i + 1, len(intervals)):
                a2, b2 = intervals[j]
                if a2 <= a1 and b1 <= b2:
                    covered.add(i)
                elif a1 <= a2 and b2 <= b1:
                    covered.add(j)
        return len(intervals) - len(covered)
