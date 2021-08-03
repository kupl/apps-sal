class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        q, nq, d, vis = {(0,0)}, set(), {(0,0):(0,0)}, set()
        # import numpy as np
        # A = np.zeros((len(grid),len(grid[0])))
        # for i,j in itertools.product(range(len(grid)),range(len(grid[0]))):
        #     A[i,j] = grid[i][j]
        while q:
            vis = set.union(vis,q)
            for i,j in q:
                # print(\"\
parent node:\",i,j)
                for m,n in [(i-1,j),(i,j-1),(i+1,j),(i,j+1)]:
                    in_grid = 0<=m<len(grid) and 0<=n<len(grid[0])
                    dist, obst = d[(i,j)]
                    if in_grid:
                        obst += 1 if grid[m][n]==1 else 0
                        if obst < d.get((m,n),(0,float('inf')))[1]:
                            d[(m,n)] = (dist+1,obst)
                            nq.add((m,n))
                    x, y = d.get((len(grid)-1, len(grid[0])-1),(0,float('inf')))
                    if y <= k:
                        return x
            q, nq = nq, set()
        return -1
