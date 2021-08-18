class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        d = {}
        for l, r in intervals:
            if l not in d:
                d[l] = []
            d[l].append(r)
        dd = []
        for l in sorted(d.keys()):
            dd.append([l, max(d[l])])
        for i in range(len(dd)):
            for j in range(i + 1, len(dd)):
                if dd[i] and dd[j] and dd[i][1] >= dd[j][1]:
                    dd[j] = False
        ans = 0
        for ddd in dd:
            if ddd:
                ans += 1
        return ans
