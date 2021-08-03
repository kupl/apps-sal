class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        point_set = set()
        points.sort()
        for point in points:
            point_set.add((point[0], point[1]))
        
        min_area = math.inf
        N = len(points)
        for i in range(N):
            start_point = points[i]
            for j in range(i+1,N):
                end_point = points[j]
                if end_point[0] > start_point[0] and end_point[1] > start_point[1]:
                    area = (end_point[0]-start_point[0])*(end_point[1]-start_point[1])
                    if area < min_area and \\
                       (start_point[0], end_point[1]) in point_set and \\
                       (end_point[0], start_point[1]) in point_set:
                        min_area = area
                
        return min_area if min_area != math.inf else 0
            
        
