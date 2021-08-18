class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        vsides = dict()
        for x, y in points:
            if x in vsides:
                vsides[x].append(y)
            else:
                vsides[x] = [y]
        slengths = dict()
        min_area = float('inf')
        xs = list(vsides.keys())
        xs.sort()
        for x in xs:
            vs = vsides[x]
            vs.sort()
            for i in range(len(vs) - 1):
                for j in range(i + 1, len(vs)):
                    if (vs[i], vs[j]) in slengths:
                        area = abs((x - slengths[(vs[i], vs[j])]) * (vs[j] - vs[i]))
                        min_area = min(min_area, area)
                    slengths[(vs[i], vs[j])] = x
        return min_area if min_area != float('inf') else 0
