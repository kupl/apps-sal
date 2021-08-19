class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        l = len(intervals)
        # sorting the list so each element can only be compared with next element
        intervals.sort(key=lambda sl: sl[0], reverse=True)
        # remove duplicate elements
        res = l
        print(intervals)
        for i in range(l - 1, 0, -1):
            if (intervals[i - 1][0] >= intervals[i][0] and intervals[i - 1][1] <= intervals[i][1]):
                intervals.remove(intervals[i - 1])
                print((intervals[i - 1]))
                res -= 1
        return res
