# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/discuss/451787/Python-O(m*n*k)-BFS-Solution-with-Explanation

from collections import deque

def is_valid_cell(row, col, rows, cols):
    return 0 <= row < rows and 0 <= col < cols


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        # do the normal BFS but add the parameter k for eleminations
        queue = deque()
        visited = set()
        
        rows , cols = len(grid), len(grid[0])
        start_row, start_col = 0, 0
        end_row, end_col = rows - 1, cols - 1
        
        # queue tuple will look like (row, col, eliminations, steps)
        queue.append((start_row, start_col, k, 0))
        # visited/seen tuple will look like (row, col, eliminations)
        visited.add((start_row, start_col, k))
        
        # directions
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        
        while queue:
            row, col, eliminations, steps = queue.popleft()
            # destination reached
            if row == end_row and col == end_col:
                return steps
            
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if not is_valid_cell(r, c, rows, cols):
                    continue
                # hitting obstacle
                if grid[r][c] == 1 and eliminations > 0 and (r, c, eliminations - 1) not in visited:
                    visited.add((r, c, eliminations - 1))
                    queue.append((r, c, eliminations - 1, steps + 1))
                
                # not hitting obstacle
                if grid[r][c] == 0 and (r, c, eliminations) not in visited:
                    visited.add((r, c, eliminations))
                    queue.append((r, c, eliminations, steps + 1))
        
        return -1
            
            
            
        
        

