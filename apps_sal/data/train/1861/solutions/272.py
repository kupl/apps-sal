class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        max_area = float(\"inf\")
        seen = set()
        for x1, y1 in points:
            for x2, y2 in points:
                if (x1, y2) in seen and (x2, y1) in seen:
                    area = abs(x2 - x1) * abs(y2 - y1)
                    if area != 0:
                        max_area = min(max_area, area)
            seen.add((x1, y1))
        return max_area if max_area < float(\"inf\") else 0 
