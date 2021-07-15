class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x: (x[0], - x[1]))
        endingval = 0
        res = 0
        for _,end in intervals:
            if endingval < end:
                endingval = end
                res += 1
        return res
