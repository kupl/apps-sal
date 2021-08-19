class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:

        def smallestinterval(l):
            rst = float('inf')
            for i in range(1, len(l)):
                if l[i] - l[i - 1] < rst:
                    rst = l[i] - l[i - 1]
            return rst
        xloc = defaultdict(set)
        for p in points:
            xloc[p[1]].add(p[0])
        minarea = float('inf')
        xkeys = list(xloc.keys())
        for x1 in range(len(xkeys)):
            for x2 in range(x1):
                if x1 != x2:
                    sharedy = xloc[xkeys[x1]] & xloc[xkeys[x2]]
                    if len(sharedy) > 1:
                        ally = list(sharedy)
                        ally.sort()
                        smallinterval = smallestinterval(ally)
                        if smallinterval * abs(xkeys[x1] - xkeys[x2]) < minarea:
                            minarea = smallinterval * abs(xkeys[x1] - xkeys[x2])
        if minarea == float('inf'):
            return 0
        return minarea
