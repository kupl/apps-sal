class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(reverse=True)
        intervals.sort(key=lambda i: i[1])
        covered = set()
        for (i, (c, d)) in enumerate(intervals):
            for (a, b) in intervals[0:i]:
                if b < c:
                    continue
                if c <= a and b <= d:
                    covered.add((a, b))
        return len(intervals) - len(covered)
