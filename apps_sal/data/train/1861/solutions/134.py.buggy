'''
1. When we see new x point, we establish base point x as baseX.
2. For every baseX, there will be multiple y points (y_for_baseX array)
3. If y was registered in previous base(for base in y_for_baseX), we update res.
  - In other words, we update res if (y, base) seen before at another x.
4. We also update x value of seen[base][y]
5. After processing, we append y to bases array.
6. Return res
'''

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        \"\"\"
        :type points: List[List[int]]
        :rtype: int
        \"\"\"
        min_area = float('inf')
        points_table = set()
        
        for x, y in points:
            points_table.add((x,y))
            
        for x1, y1 in points:
            for x2, y2 in points:
                if x1 > x2 and y1 > y2: # skip dupes
                    if (x1, y2) in points_table and (x2, y1) in points_table:
                        area = abs(x1 - x2) * abs(y1 - y2)
                        if area: min_area = min(area, min_area)
                        
        return 0 if min_area == float('inf') else min_area
