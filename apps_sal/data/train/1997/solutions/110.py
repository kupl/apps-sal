class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: [x[0], -x[1]])
        prev_end, count = 0, 0

        for _, curr_end in intervals:
            if prev_end < curr_end:
                count += 1
                prev_end = curr_end

        return count
