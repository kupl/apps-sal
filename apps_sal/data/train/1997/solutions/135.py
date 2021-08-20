class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        covered_intervals = set()
        for a in intervals:
            for b in intervals:
                if a is b or tuple(b) in covered_intervals:
                    continue
                if covered(a, b):
                    covered_intervals.add(tuple(a))
                    break
        return len(intervals) - len(covered_intervals)


def covered(a, b):
    return b[0] <= a[0] and a[1] <= b[1]
