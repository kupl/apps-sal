class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        if len(points) < 4:
            return 0
        
        seen = set()
        minarea = sys.maxsize
        for x1, y1 in points:
            for x2, y2 in seen:
                if (x1,y2) in seen and (x2,y1) in seen:
                    minarea = min(minarea, abs(x2-x1)*abs(y2-y1))
            seen.add((x1,y1))
        return minarea if minarea < sys.maxsize else 0
