from collections import defaultdict
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points_by_x = defaultdict(set)
        # points_by_y = defaultdict(set)
        for point in points:
            points_by_x[point[0]].add(point[1])
            # points_by_y[point[1]].add(point[0])
        
        
        xs_to_delete = []
        for x, ys in points_by_x.items():
            if len(ys) < 2:
                xs_to_delete.append(x)
        for x in xs_to_delete:
            del points_by_x[x] 
        
        \"\"\"
        ys_to_delete = []
        for y, xs in points_by_y.items():
            if len(xs) < 2:
                ys_to_delete.append(y)
        [del points_by_y[y] for y in ys_to_delete]
        \"\"\"
        # [ys.sort() for x, ys in points_by_x.items()]
        # [xs.sort() for y, xs in points_by_y.items()]
        
        minarea = float('inf')
        for x1, ys1 in points_by_x.items():
            for x2, ys2 in points_by_x.items():
                if x1 == x2:
                    continue
                xdiff = abs(x2-x1)
                if xdiff > minarea:
                    continue
                ys_common = sorted(ys1.intersection(ys2))
                if len(ys_common) < 2:
                    continue
                ydiff = min(y2-y1 for y1, y2 in zip(ys_common[:-1], ys_common[1:]))
                area = xdiff*ydiff
                if area < minarea:
                    minarea = area
        return 0 if minarea == float('inf') else minarea
        
