class Solution(object):
    def minAreaRect(self, points):
        \"\"\"
        :type points: List[List[int]]
        :rtype: int
        \"\"\"
        min_area = sys.maxsize
        points_table = set()
        
        for x, y in points:
            points_table.add((x,y))
            
        for p1,p2 in itertools.combinations(points_table,2):
               # print (p1,p2)
                x1,y1 = p1
                x2,y2 = p2 
               # if x1 > x2 and y1 > y2: # Skip looking at same point
                if 1:   
                    if (x1, y2) in points_table and (x2, y1) in points_table:
                       # print (\"wew\",p1,p2)
                        area = abs(x1 -  x2) * abs(y1 - y2)
                        if area:
                            min_area = min(area, min_area)
                        
        return 0 if min_area == sys.maxsize else min_area
