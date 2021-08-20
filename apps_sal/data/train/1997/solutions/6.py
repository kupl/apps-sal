class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        ordered_intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
        candidates = set()
        for i in range(len(intervals)):
            (curr_start, curr_end) = ordered_intervals[i]
            for j in range(i + 1, len(intervals)):
                (next_start, next_end) = ordered_intervals[j]
                if next_start >= curr_end:
                    break
                if next_end <= curr_end:
                    candidates.add(j)
        return len(intervals) - len(candidates)
