class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(reverse=True)
        temp = []
        for i in range(n - 1, -1, -1):
            for k in range(0, n):
                if (i != k) and (intervals[k][0] <= intervals[i][0] and intervals[i][1] <= intervals[k][1]):
                    temp.append(intervals[i])
                    break

        res = [i for i in intervals if i not in temp]
        return len(res)
