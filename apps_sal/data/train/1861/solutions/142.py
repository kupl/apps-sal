class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        ys = {}
        for x, y in points:
            if y not in ys:
                ys[y] = set()
            ys[y].add(x)                
        result = -1            
        for y1 in ys:
            for y2 in ys:
                if y1 == y2:
                    continue
                points = ys[y1].intersection(ys[y2])                      
                if len(points) < 2:
                    continue
                points = list(points)                    
                points.sort()
                x1 = points[0]
                for i in range(1, len(points)):
                    x2 = points[i]
                    area = (x2-x1) * abs(y2 - y1)
                    if result < 0:
                        result = area
                    else:
                        result = min(area, result)
                    x1 = x2                        
                        
        return result if result >= 0 else 0                                

