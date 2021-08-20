class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if intervals[i][0] > intervals[j][0]:
                    (intervals[i], intervals[j]) = (intervals[j], intervals[i])
                elif intervals[i][0] == intervals[j][0]:
                    if intervals[i][1] < intervals[j][1]:
                        (intervals[i], intervals[j]) = (intervals[j], intervals[i])
        l = []
        print(intervals)
        for i in intervals:
            if l == []:
                l.append(i)
            else:
                k1 = l[-1]
                k2 = i
                if k1[0] <= k2[0] and k1[1] >= k2[1]:
                    continue
                else:
                    l.append(i)
        return len(l)
