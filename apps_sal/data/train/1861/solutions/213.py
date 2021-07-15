class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        \"\"\"
        |
        |  *       *   
        |       *
        |  *       *
        |_______________
        
        
        
        
        \"\"\"
        
        min_x = float('inf')
        max_x = float('-inf')
        
        points_dict = dict()
        left_sides = dict()
        
        for point in points:
            min_x = min(min_x, point[0])
            max_x = max(max_x, point[0])
        
            if point[0] not in points_dict:
                points_dict[point[0]] = [point]
            else:
                points_dict[point[0]].append(point)
        
        min_area = float('inf')
        
        
        for x in range(min_x, max_x + 1):
            if x in points_dict:
                for point in points_dict[x]:
                    for point2 in points_dict[x]:
                        if (point[1], point2[1]) in left_sides:
                            min_area = min(min_area, abs(point[1] - point2[1]) * abs(point[0] - left_sides[point[1], point2[1]]))

                        if point != point2:
                            left_sides[point[1], point2[1]] = x
        
        return 0 if min_area == float('inf') else min_area
