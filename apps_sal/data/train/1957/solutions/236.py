class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        q = collections.deque([[0, 0, 0]])    # row, col, num of obstables met so far
        visited = {(0, 0): 0}                 # row, col   =>   num of obstables met so far
        steps = 0
        
        while q:
            size = len(q)
            for _ in range(size):
                r, c, obs = q.popleft()
                if obs > k: continue
                if r == m - 1 and c == n - 1: 
                    return steps
                for r2, c2 in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
                    if 0 <= r2 < m and 0 <= c2 < n:
                        next_obs = obs + 1 if grid[r2][c2] == 1 else obs
                        if next_obs < visited.get((r2, c2), float('inf')):
                            visited[(r2, c2)] = next_obs
                            q.append([r2, c2, next_obs])
            steps += 1
        
        return -1
