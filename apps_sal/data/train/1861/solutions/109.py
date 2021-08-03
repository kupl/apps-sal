class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        globalMinArea = float('inf')
        a = set()
        for x, y in points:
            for x1, y1 in a:
                if (x, y1) in a and (x1, y) in a:
                    currentMinArea = abs(x - x1) * abs(y - y1)
                    globalMinArea = min(globalMinArea, currentMinArea)
            a.add((x, y))
        return globalMinArea if globalMinArea < float('inf') else 0
