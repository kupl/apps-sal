class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return -1
        
        # Main idea: run Dijkstra's except only expand on nodes
        # that do not have a wall on the oposite side of the
        # box location.
        self.grid = grid
        dst = None
        start = None
        box_start = None
        from queue import PriorityQueue
        pq = PriorityQueue()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                elem = grid[row][col]
                if elem == \"B\":
                    box_start = (row, col)
                elif elem == \"T\":
                    dst = (row, col)
                elif elem == \"S\":
                    start = (row, col)
        
        assert dst is not None
        assert start is not None
        assert box_start is not None
        pq.put((0, box_start[0], box_start[1], start))
        
        best = {}
        while not pq.empty():
            pushes, row, col, start = pq.get()
            if (row, col, start) not in best or best.get((row, col, start), float(\"inf\")) > pushes:
                best[(row, col, start)] = pushes
                if (row, col) == dst:
                    return pushes
                if row + 1 < len(grid) and row - 1 >= 0:
                    if grid[row + 1][col] != \"#\" and grid[row - 1][col] != \"#\" and self.dfs(start[0], start[1], (row +1, col), set(), (row, col)):
                        pq.put((pushes + 1, row - 1, col, (row, col)))
                    if grid[row - 1][col] != \"#\" and grid[row + 1][col] != \"#\" and self.dfs(start[0], start[1], (row - 1, col), set(), (row, col)):
                        pq.put((pushes + 1, row + 1, col, (row, col)))
                if col + 1 < len(grid[0]) and col - 1 >= 0:
                    if grid[row][col + 1] != \"#\" and grid[row][col - 1] != \"#\" and self.dfs(start[0], start[1], (row , col + 1), set(), (row, col)):
                        pq.put((pushes + 1, row, col - 1, (row, col)))
                    if grid[row][col - 1] != \"#\" and grid[row][col + 1] != \"#\" and self.dfs(start[0], start[1], (row , col - 1), set(), (row, col)):
                        pq.put((pushes + 1, row, col + 1, (row, col)))
        return -1
    
    def dfs(self, r, c, goal, seen, box_location):
        if (r, c) == goal:
            return True
        if not (0 <= r < len(self.grid)):
            return False
        if not (0 <= c < len(self.grid[0])):
            return False
        if self.grid[r][c] == \"#\":
            return False
        if (r, c) == box_location:
            return False
        if (r, c) not in seen:
            seen.add((r, c))
            if self.dfs(r + 1, c, goal, seen, box_location):
                return True
            if self.dfs(r - 1, c, goal, seen, box_location):
                return True
            if self.dfs(r, c + 1, goal, seen, box_location):
                return True
            if self.dfs(r, c - 1, goal, seen, box_location):
                return True
        return False
