class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        int_set = set(tuple(i) for i in intervals)
        for i, (a, b) in enumerate(intervals):
            for c, d in intervals[i + 1:]:
                if a <= c and d <= b and (c, d) in int_set:
                    int_set.remove((c, d))
                elif c <= a and b <= d and (a, b) in int_set:
                    int_set.remove((a, b))
        return len(int_set)
