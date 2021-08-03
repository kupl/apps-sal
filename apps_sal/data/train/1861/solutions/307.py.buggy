class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        visited = set()
        res = float(\"inf\")
        for x1, y1 in points:
            for x2, y2 in visited:
                if (x1, y2) in visited and (x2, y1) in visited:
                    res = min(res, abs(x2 - x1) * abs(y2 - y1))
                    
            visited.add((x1, y1))
        return res if res != float(\"inf\") else 0
                
