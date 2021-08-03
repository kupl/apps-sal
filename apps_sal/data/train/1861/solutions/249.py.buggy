class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        n = len(points)
        point_set = {(x, y) for x, y in points}
        min_area = float(\"inf\")
        
        for i in range(n-1):
            for j in range(i+1, n):
                x0, y0 = points[i]
                x1, y1 = points[j]
                
                if x0 != x1 and y0 != y1:
                    if (x0, y1) in point_set and (x1, y0) in point_set:
                        area = abs((x1-x0)*(y1-y0))
                        min_area = min(area, min_area)
                    
        return min_area if min_area < float(\"inf\") else 0

# time: O(n^2)
# space: O(n)
