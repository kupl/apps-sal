class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        x_to_points = defaultdict(lambda: [])
        y_to_points = defaultdict(lambda: set())
        for [x, y] in points:
            x_to_points[x].append((x, y))
            y_to_points[y].add((x, y))
            
        min_rect = float('inf')
        for x in sorted(x_to_points.keys()):
            xpoints = x_to_points[x]
            if len(xpoints) < 2:
                continue
            
            for x1_index in range(len(xpoints)):
                for x2_index in range(x1_index + 1, len(xpoints)):
                    x1, y1 = xpoints[x1_index]
                    x2, y2 = xpoints[x2_index]
                    for x3, y3 in y_to_points[y1]:     
                        if x3 == x2:
                            continue
                        if (x3, y2) in y_to_points[y2]:
                            min_rect = min(min_rect, abs(y2-y1)*abs(x3-x2))
            
        
        return 0 if min_rect  == float('inf') else min_rect

