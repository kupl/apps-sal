class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        covered = 0
        m = {}
        for [l, r] in intervals:
            if l not in m:
                m[l] = r
            else:
                m[l] = max(r, m[l])
                covered += 1

        a = []
        for i in m:
            a.append([i, m[i]])

        a.sort(key=lambda x: x[0])
        # print(a)
        _c = set()
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if a[j][1] <= a[i][1] and j not in _c:
                    _c.add(j)
                    covered += 1

        return len(intervals) - covered
