class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        \"\"\"
        (x, y, 3)
        
        (x1, y1, 1) (x2, y2, 1)
        \"\"\"
        def get_neighs(cell, grid):
            M = len(grid)
            N = len(grid[0])
            deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            result = []
            for delta in deltas:
                new_cell = (cell[0]+delta[0], cell[1]+delta[1])
                if 0 <= new_cell[0] < M and 0 <= new_cell[1] < N:
                    result.append(new_cell)
            return result
        
        q = [(((0, 0), k), 0)]
        M = len(grid)
        N = len(grid[0])
        
        visited = set()
        while q:
            state, step_cnt = q.pop(0)
            if state in visited:
                continue
            
            visited.add(state)
            cell, remaining_power = state
            if cell[0] == M-1 and cell[1] == N-1:
                return step_cnt
            
            if grid[cell[0]][cell[1]] == 1:
                if remaining_power <= 0:
                    continue
                else:
                    remaining_power -= 1
            
            for neigh in get_neighs(cell, grid):
                if (neigh, remaining_power) not in visited:
                    q.append(((neigh, remaining_power), step_cnt+1))
        
        return -1
