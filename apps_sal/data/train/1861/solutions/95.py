class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        n = len(points)
        nx = len(set(x for x, y in points))
        ny = len(set(y for x, y in points))
        
        p = collections.defaultdict(list)
        lastseen = {}
        if nx > ny:
            for x, y in points:
                p[x].append(y)
        else:
            for x, y in points:
                p[y].append(x)
                
        minarea =float(\"inf\")     
        for x in sorted(p):
            p[x].sort()
            for i in range(len(p[x])):
                for j in range(i):
                    y1,y2 = p[x][i], p[x][j]
                    if (y1,y2) in lastseen:
                        area = abs(y1-y2) * abs(x-lastseen[(y1,y2)])
                        minarea = min(area,minarea)
                    lastseen[(y1,y2)] = x
        #print(lastseen)
        return minarea if minarea < 10**21 else 0
