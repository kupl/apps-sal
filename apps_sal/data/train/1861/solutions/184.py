class Solution:
    def minAreaRect(self, points):
        \"\"\"
        * loose criteria, just check all pairs of points.
        * set is faster than list
        \"\"\"
        seen = set()
        res = float('inf')
        for x1, y1 in points:
            for x2, y2 in seen:
                if (x1, y2) in seen and (x2, y1) in seen:
                    area = abs(x1 - x2) * abs(y1 - y2)
                    res = min(res, area)
                    # if area and area < res:
                    #     res = area
            seen.add((x1, y1))
        return res if res < float('inf') else 0
    
        ### TLE
        # res = float('inf')
        # for i, (x1, y1) in enumerate(points):
        #     for x2, y2 in points[i:]:
        #         if [x1, y2] in points and [x2, y1] in points:
        #             area = abs(x1 - x2) * abs(y1 - y2)
        #             if area and area < res:
        #                 res = area
        #     #seen.add((x1, y1))
        # return res if res < float('inf') else 0
    


        
