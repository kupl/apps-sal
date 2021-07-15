class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if len(points) == 1: return 0
        res = 0
        curr = 0 # select a random point as the starting point
        dis = [math.inf] * n
        explored = set()
        
        for i in range(n - 1):
            x0, y0 = points[curr]
            explored.add(curr)
            for j, (x, y) in enumerate(points):
                if j in explored: continue
                dis[j] = min(dis[j], abs(x - x0) + abs(y - y0))
                
            delta, curr = min((d, j) for j, d in enumerate(dis)) 
            dis[curr] = math.inf
            res += delta
            
        return res
        n = len(p)
        if n == 1: return 0

        dist = [[10**30 for x in range(n)] for x in range(n)]
        for i in range(n):
            for j in range(i+1,n):
                dist[i][j] = dist[j][i] = abs(p[i][0]-p[j][0]) + abs(p[i][1]-p[j][1])

        fin = set()
        cur = 0
        ret = 0
        for i in range(n-1):
            fin.add(cur)
            (temp,j) = min( (x, i) for i, x in enumerate(dist[cur]) )
            ret += temp
            dist[cur][j] = dist[j][cur] = 10**30
            cur = j
            print(fin,cur,temp)
            
        
        return ret
                
        
        return self.dp(dist)

    def dp(self, dist:List[List[int]]) -> int:
        n = len(dist)
        if n == 2:
            return dist[0][1]

        mi = 10**15
        for i in range(1,n):
            dd = [x.copy() for x in dist]
            for j in range(1,n):
                if j == i: continue
                dd[0][j] = dd[j][0] = min(dist[0][j], dist[i][j])
            dd = dd[:i]+dd[i+1:n]
            dd = [ x[:i]+x[i+1:n] for x in dd]
            mi = min(self.dp(dd)+dist[0][i], mi)
        return mi
