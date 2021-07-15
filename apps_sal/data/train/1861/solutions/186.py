class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        seen = set()
        output = float('inf')
        
        for x1, y1 in points:
            for x2, y2 in seen:
                if (x1, y2) in seen and (x2, y1) in seen:
                    area = abs(x1-x2) * abs(y1-y2)
                    if area > 0 and area < output:
                        output = area
            seen.add((x1,y1))
        return output if output < float('inf') else 0
