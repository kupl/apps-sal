from functools import cmp_to_key


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        def cmp_intervals(left, right):
            if left[0] == right[0]:
                return right[1] - left[1]
            return left[0] - right[0]

        n = len(intervals)
        s_intervals = sorted(intervals, key=cmp_to_key(cmp_intervals))
        covered = set()

        for i in range(n - 1):
            a, b = s_intervals[i]

            for j in range(i + 1, n):
                c, d = s_intervals[j]

                if a <= c and d <= b:
                    covered.add((c, d))

        return n - len(covered)
