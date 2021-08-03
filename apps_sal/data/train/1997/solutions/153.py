class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        i = 0
        length = len(intervals)
        while i < length:
            flag = True
            j = i + 1
            while j < length:
                if intervals[j][0] <= intervals[i][0] and intervals[i][1] <= intervals[j][1]:
                    intervals.pop(i)
                    length -= 1
                    i = max(i - 1, 0)
                    if i == 0:
                        flag = False
                elif intervals[i][0] <= intervals[j][0] and intervals[j][1] <= intervals[i][1]:
                    intervals.pop(j)
                    length -= 1
                    i = max(i - 1, 0)
                    if i == 0:
                        flag = False
                else:
                    j += 1
            if flag:
                i += 1
        return length
