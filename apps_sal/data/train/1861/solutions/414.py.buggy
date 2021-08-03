from collections import defaultdict
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        columns = defaultdict(list)
        for x, y in points:
            columns[x].append(y)
        seen = {}
        min_area = float(\"inf\")
        for col, ys in sorted(columns.items()):
            ys = sorted(ys)
            for i, y1 in enumerate(ys):
                for y2 in ys[i+1:]:
                    if (y1, y2) in seen:
                        #we have a rectangle
                        x1 = seen[(y1, y2)]
                        area = (col -x1) * (y2-y1)
                        min_area = min(min_area, area)
                        
                        
                    seen[(y1, y2)] = col
        return 0 if min_area == float(\"inf\") else min_area
                    
        
