class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        c = 0
        for i in intervals:
            for j in intervals:
                c += 1
        a = sorted(sorted(intervals, key=itemgetter(1), reverse=True), key=itemgetter(0))
        i = 0
        while i < len(a):
            j = i + 1
            while j < len(a) and a[j][0] >= a[i][0] and (a[j][1] <= a[i][1]):
                a.pop(j)
            i = j
        return len(a)
