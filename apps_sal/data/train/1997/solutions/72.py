class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        exclusion_set = set()
        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                a, b = intervals[i]
                c, d = intervals[j]
                if c <= a and b <= d:
                    exclusion_set.add((a, b))
                if a <= c and d <= b:
                    exclusion_set.add((c, d))
        return len(intervals) - len(exclusion_set)
