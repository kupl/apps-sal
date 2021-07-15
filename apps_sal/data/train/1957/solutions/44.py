from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        queue = deque([(0, 0, 0, 0)])
        visited = set()
        visited.add((0, 0, 0))
        m = len(grid)
        n = len(grid[0])
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

        while queue:
            r, c, removed, count = queue.popleft()

            if r == m - 1 and c == n - 1:
                return count
            
            for inc_r, inc_c in directions:
                new_r = r + inc_r
                new_c = c + inc_c
                
                if 0 <= new_r < m and 0 <= new_c < n:
                    if removed < k and (new_r, new_c, removed+1) not in visited and grid[new_r][new_c] == 1:
                        queue.append((new_r, new_c, removed+1, count+1))
                        visited.add((new_r, new_c, removed+1))
                    elif (new_r, new_c, removed) not in visited and grid[new_r][new_c] == 0:
                        queue.append((new_r, new_c, removed, count+1))
                        visited.add((new_r, new_c, removed))

        return -1
