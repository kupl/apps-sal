class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points_set = set([(point[0], point[1]) for point in points])
        min_area = float(\"inf\")
        for i, point1 in enumerate(points):
            for j in range(i):
                point2 = points[j]
                if point1[0] != point2[0] and point1[1] != point2[1] and (point1[0], point2[1]) in points_set and (point2[0], point1[1]) in points_set:
                    min_area = min(min_area, abs(point2[0]-point1[0])*abs(point2[1]-point1[1]))
        return min_area if min_area < float('inf') else 0
                    
                
            
        
