class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        if len(points) < 4:
            return 0
        
        area = float('inf')
        seen = set()
        for x1, y1 in points:
            for x2, y2 in seen:
                if (x1, y2) in seen and (x2, y1) in seen:
                    l, w = abs(x1 - x2), abs(y1 - y2)
                    area = min(area, l*w)
                        
            seen.add((x1, y1))
        
        return area if area < float('inf') else 0
