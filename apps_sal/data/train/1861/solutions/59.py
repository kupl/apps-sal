class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 4:
            return 0
        s = set([tuple(i) for i in points])
        d = {}
        for i in points:
            if i[0] in d:
                d[i[0]].append(i[1])
            else:
                d[i[0]] = [i[1]]
        for i in list(d.keys()):
            if len(d[i]) == 1:
                d.pop(i)
        dkeys = list(d.keys())
        minarea = float('inf')
        for i in range(len(dkeys) - 1):
            if len(points[i]) == 1:
                continue

            for x in range(len(d[dkeys[i]]) - 1):
                for y in range(x + 1, len(d[dkeys[i]])):
                    for j in range(i + 1, len(dkeys)):
                        if (dkeys[j], d[dkeys[i]][x]) in s and (dkeys[j], d[dkeys[i]][y]) in s:
                            minarea = min(minarea, abs(dkeys[i] - dkeys[j]) * abs(d[dkeys[i]][x] - d[dkeys[i]][y]))

        if minarea == float('inf'):
            return 0
        return minarea
