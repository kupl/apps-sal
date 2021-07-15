class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        seen = set()
        res = float('inf')
        for point in points:                                                    
            x, y = point[0], point[1]            
            for _x, _y in seen:
                if (x, _y) in seen and (_x, y) in seen:
                    res = min(res, abs(x - _x) * abs(y - _y))
            seen.add((x, y))
            
        if res == float('inf'):
            return 0
        return res
                

            
            
'''
    def minAreaRect(self, points):
        n = len(points)
        nx = len(set(x for x, y in points))
        ny = len(set(y for x, y in points))
        if nx == n or ny == n:
            return 0

        p = collections.defaultdict(list)
        if nx > ny:
            for x, y in points:
                p[x].append(y)
        else:
            for x, y in points:
                p[y].append(x)

        lastx = {}
        res = float('inf')
        for x in sorted(p):
            p[x].sort()
            for i in range(len(p[x])):
                for j in range(i):
                    y1, y2 = p[x][j], p[x][i]
                    if (y1, y2) in lastx:
                        res = min(res, (x - lastx[y1, y2]) * abs(y2 - y1))
                    lastx[y1, y2] = x
        return res if res < float('inf') else 0

'''
        
        
            
            

