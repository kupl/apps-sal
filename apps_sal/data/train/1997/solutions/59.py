class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        rm = {}
        for i in range(1, len(intervals)):
            for ((a, b), (c, d)) in zip(intervals[0:-i], intervals[i:]):
                if a >= c:
                    if b <= d:
                        rm[a, b] = True
                elif c >= a:
                    if d <= b:
                        rm[c, d] = True
        return len(intervals) - len(rm)
