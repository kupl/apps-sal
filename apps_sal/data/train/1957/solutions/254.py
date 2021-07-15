class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        dist = []
        for i in range(n):
            dist.append([])
            for j in range(m):
                dist[i].append([-1,-1])
        queue = []
        queue.append([0, 0, 0, k])
        dist[0][0][0] = 0
        dist[0][0][1] = k
        while queue:
            top = queue.pop(0)
            dis = top[0]
            i = top[1]
            j = top[2]
            if i==n-1 and j ==m-1:
                return dis
            res = top[3]
            print(i, j, dis, res)
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if x >= 0 and y >= 0 and x < n and y < m:
                    nk = res - int(grid[x][y] == 1)
                    if nk >= 0:
                        if dist[x][y][0] == -1 or nk > dist[x][y][1]:
                            dist[x][y][0] = dis+1
                            dist[x][y][1] = nk
                            queue.append([dis+1, x, y, nk])
        
        return dist[n-1][m-1][0]
