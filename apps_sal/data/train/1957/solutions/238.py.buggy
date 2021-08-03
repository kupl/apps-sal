from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        \"\"\"
        BFS
        
        visited: {i, j, # of breaks}
        
        q = [(i, j, # of breaks, # of steps)]
        generate neighbor:
            if grid[nei] == 1:
                (i, j, # of breaks + 1)
                discard if # of breaks + 1 > k
            else:
                (i, j, # of breaks)
        \"\"\"
        q = deque([(0, 0, grid[0][0], 0)])
        visited = {(0, 0): grid[0][0]}
        m, n = len(grid), len(grid[0])
        if m == n == 1:
            return 0
        while q:
            i, j, breakNumber, steps = q.popleft()
            for ni, nj in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
                if 0 <= ni < m and 0 <= nj < n:
                    nBreaks = breakNumber + grid[ni][nj]
                    if nBreaks > k:
                        continue
                    if (ni, nj) == (m-1, n-1):
                        return steps + 1
                    if (ni, nj) not in visited or visited[(ni, nj)] > nBreaks:
                        visited[(ni, nj)] = nBreaks
                        q.append((ni, nj, nBreaks, steps + 1))
        return -1
