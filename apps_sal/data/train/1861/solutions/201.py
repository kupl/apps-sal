class Solution:
    def minAreaRect(self, points):
        \"\"\"
        :type points: List[List[int]]
        :rtype: int
        In order to form a rectangle, you need four points all positioned at 90 degrees to each other.
        In this approach, we store all given points in a set.Then iteratively go through all the points in two loops (x1, y1) and (x2, y2) while checking if (x1, y2) and (x2, y1) are also valid points. If so, we found a rectangle.We calculate the area of this rectangle. If this area is smaller than the minimum area seen so far, make it the minimum area.
        
        \"\"\"
        min_area = sys.maxsize
        points_table = set()
        
        for x, y in points:
            points_table.add((x,y))
            
        for x1, y1 in points:
            for x2, y2 in points:
                if x1 > x2 and y1 > y2:
                    # Skip looking at same point
                    if (x1, y2) in points_table and (x2, y1) in points_table:
                        area = abs(x1 -  x2) * abs(y1 - y2)
                        if area:
                            min_area = min(area, min_area)
                        
        return 0 if min_area == sys.maxsize else min_area
