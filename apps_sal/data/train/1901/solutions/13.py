class DSU:
    def __init__(self, N):
        self.par = [i for i in range(N)]
        self.cnt = N
    def find(self, i):
        if self.par[i] != i:
            self.par[i] = self.find(self.par[i])
        return self.par[i]
    def union(self, i, j):
        pi = self.find(i)
        pj = self.find(j)
        if pi != pj:
            self.par[pi] = pj
            self.cnt-=1
        
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        dsu = DSU(R*C)
        dirs = [[1,0], [0,1],[-1,0], [0,-1]]
        for y in range(R):
            for x in range(C):
                if grid[y][x] == 1:
                    for dx,dy in dirs:
                        nx , ny = dx+x, dy+y
                        if 0<=nx<C and 0<=ny<R and grid[ny][nx] == 1:
                            dsu.union(y*R+x, ny*R+nx)
        smap = {}
        for y in range(R):
            for x in range(C):
                if grid[y][x] == 1:
                    r = dsu.find(y*R+x)
                    if r in smap:
                        smap[r] += 1
                    else:
                        smap[r] = 1
        ans = 0
        for y in range(R):
            for x in range(C):
                if grid[y][x] == 0:
                    rset = set()
                    for dx, dy in dirs:
                        nx , ny = dx+x, dy+y
                        if 0<=nx<C and 0<=ny<R and grid[ny][nx] == 1:
                            r = dsu.find(ny*R+nx)
                            rset.add(r)
                    t = 1
                    for r in rset:
                        t+=smap[r]
                    ans = max(ans, t)
        return ans if ans != 0 else R*C

