class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        n = len(points)
        min_area = float(\"inf\")
        point_set = {(x, y) for x, y in points}
        
        for i in range(n-1):
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                if x1 != x2 and y1 != y2 and (x1, y2) in point_set and (x2, y1) in point_set:
                    min_area = min(min_area, abs((y2-y1)*(x2-x1)))
                    
        return min_area if min_area < float(\"inf\") else 0
                
