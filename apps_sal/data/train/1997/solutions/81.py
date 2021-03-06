class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        i = 0
        result = len(intervals)
        while i < len(intervals) - 1:
            (a1, b1) = intervals[i]
            j = i + 1
            remove_i = False
            while j < len(intervals):
                (a2, b2) = intervals[j]
                if a2 >= a1 and b2 <= b1:
                    intervals = intervals[:j] + intervals[j + 1:]
                    result -= 1
                    continue
                if a1 >= a2 and b1 <= b2:
                    intervals = intervals[:i] + intervals[i + 1:]
                    result -= 1
                    remove_i = True
                    break
                j = j + 1
            if remove_i:
                continue
            i += 1
        return result
