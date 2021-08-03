import collections


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        sameX = collections.defaultdict(list)
        for x, y in points:
            sameX[x].append(y)
        lastX = {}
        minArea = float('inf')
        for x in sorted(sameX):
            sameX[x].sort()
            for i in range(len(sameX[x])):
                for j in range(i):
                    y1, y2 = sameX[x][j], sameX[x][i]
                    if (y1, y2) in lastX:
                        minArea = min(minArea, (y2 - y1) * (x - lastX[y1, y2]))
                    lastX[y1, y2] = x
        return minArea if minArea != float('inf') else 0
