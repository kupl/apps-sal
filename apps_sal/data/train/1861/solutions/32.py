class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        n = len(points)
        nx = len(set(x for x, _ in points))
        ny = len(set(y for _, y in points))
        if nx == n and ny == n:
            return False
        
        p = collections.defaultdict(list)
        if nx > ny:
            for x, y in points:
                p[x].append(y)
        else:
            for x, y in points:
                p[y].append(x)
        
        last_x = {}
        area = float('inf')
        
        for x in sorted(p):
            p[x].sort()
            for i in range(len(p[x])):
                for j in range(i):
                    y1, y2 = p[x][j], p[x][i]
                    
                    if (y1, y2) in last_x:
                        area = min(area, (x - last_x[(y1, y2)]) * (y2 - y1))
                    last_x[(y1, y2)] = x
        return area if area < float('inf') else 0
