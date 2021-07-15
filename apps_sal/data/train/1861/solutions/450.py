class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        x_map= {}
        points.sort(key=lambda x: x)
        area = float('inf')
        
        y_map = {}
        
        for point in points:
            if point[0] in x_map:
                x_map[point[0]].append(point[1])
                continue
            x_map[point[0]] = [point[1]]
            
        for x in x_map:
            x_map[x].sort()
            for j in range(0, len(x_map[x])):
                y2 = x_map[x][j]
                for k in range(0, j):
                    y1 =x_map[x][k]
                    if (y1, y2) in y_map:
                        area = min(area, (y2-y1) * (x - y_map[(y1, y2)]))
                    y_map[(y1, y2)] = x
        return area if area!=float('inf') else 0
                    
                
        
        

