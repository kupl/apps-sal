class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        xtoy = collections.defaultdict(set)
        for (x, y) in points:
            xtoy[x].add(y)
        minarea = sys.maxsize
        for x1 in xtoy:
            for x2 in xtoy:
                if x1 >= x2:
                    continue
                commony = list(xtoy[x1].intersection(xtoy[x2]))
                if len(commony) < 2:
                    continue
                commony.sort()
                width = x2 - x1
                height = commony[1] - commony[0]
                for i in range(2, len(commony)):
                    height = min(height, commony[i] - commony[i - 1])
                minarea = min(minarea, height * width)
        return minarea if minarea != sys.maxsize else 0
