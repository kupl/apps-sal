class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        for i in range(0, len(intervals) - 1):
            minel = intervals[i]
            minid = i
            for j in range(i + 1, len(intervals)):
                evl = intervals[j]
                if evl[0] < minel[0]:
                    minel = evl
                    minid = j
            (intervals[i], intervals[minid]) = (intervals[minid], intervals[i])
        c = 0
        prevl = intervals[0][0]
        prevh = intervals[0][1]
        for x in range(1, len(intervals)):
            curl = intervals[x][0]
            curh = intervals[x][1]
            if curh <= prevh:
                c = c + 1
                continue
            if curl == prevl:
                c = c + 1
                if curh > prevh:
                    prevh = curh
                continue
            prevl = curl
            prevh = curh
        return len(intervals) - c
