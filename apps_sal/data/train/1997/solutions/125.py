class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        removed = 0
        for i in range(len(intervals)):
            for j in range(len(intervals)):
                if i == j:
                    continue
                print(i, j)
                a, b = intervals[i]
                c, d = intervals[j]
                if c <= a and b <= d:
                    removed += 1
                    break

        return len(intervals) - removed


class Solution1:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)

        l, r = intervals[0]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if end <= r:
                r = end
            else:

                pass
