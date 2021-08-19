class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Sort by start point
        # If two intervals shgare the same start point, put the longer one to be first
        intervals.sort(key=lambda x: (x[0], -x[1]))
        count = 0

        prev_end = 0
        for _, end in intervals:
            # if current interval is not covered
            # by the previos one
            if end > prev_end:
                count += 1
                prev_end = end

        return count
