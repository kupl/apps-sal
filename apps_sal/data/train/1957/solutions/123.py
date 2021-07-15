class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        K = k
        q = []
        q.append((0, 0, K, 0))
        seen = set()
        
        while q:
            q2 = []
            for i, j, k, c in q:
                if i == m-1 and j == n-1:
                    return c
                for ii, jj in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if 0 <= ii < m and 0 <= jj < n:
                        if grid[ii][jj] == 0 and (ii, jj, k) not in seen:
                            seen.add((ii, jj, k))
                            q2.append((ii, jj, k, c+1))
                        if grid[ii][jj] == 1 and k > 0 and (ii, jj, k-1) not in seen:
                            seen.add((ii, jj, k-1))
                            q2.append((ii, jj, k-1, c+1))
            q = q2
        return -1
    
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        K = k
        q = []
        q.append((0, 0, K, 0))
        seen = {}
        
        while q:
            q2 = []
            for i, j, k, c in q:
                if i == m-1 and j == n-1:
                    return c
                for ii, jj in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if 0 <= ii < m and 0 <= jj < n:
                        if grid[ii][jj] == 0 and ((ii, jj) not in seen or k > seen[(ii, jj)]):
                            seen[(ii, jj)] = k
                            q2.append((ii, jj, k, c+1))
                        if grid[ii][jj] == 1 and k > 0 and ((ii, jj) not in seen or k-1 > seen[(ii, jj)]):
                            seen[(ii, jj)] = k-1
                            q2.append((ii, jj, k-1, c+1))
            q = q2
        return -1
    
    # bidirection bfs
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        K = k
        q1, q2 = {}, {}
        q1[(0, 0)] = 0
        q2[(m-1, n-1)] = 0
        level = 0
        seen1, seen2 = {}, {}
        seen1[(0, 0)] = 0
        seen2[(m-1, n-1)] = 0
        
        while q1 and q2:
            tmp = {}
            if len(q2) < len(q1):
                q1, q2 = q2, q1
                seen1, seen2 = seen2, seen1
            for (i, j), k in q1.items():
                if (i, j) in q2 and k+q2[(i, j)] <= K:
                    return level
                for ii, jj in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if 0 <= ii < m and 0 <= jj < n:
                        if grid[ii][jj] == 0 and ((ii, jj) not in seen1 or k < seen1[(ii, jj)]):
                            seen1[(ii, jj)] = k
                            tmp[(ii, jj)] = k
                        if grid[ii][jj] == 1 and k < K and ((ii, jj) not in seen1 or k+1 < seen1[(ii, jj)]):
                            seen1[(ii, jj)] = k+1
                            tmp[(ii, jj)] = k+1
            q1 = tmp
            level += 1
        return -1
