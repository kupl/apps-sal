class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        \"\"\"
        [[1,1,1,1,1],
         [1,0,0,0,1],
         [1,0,1,0,1],
         [1,0,0,0,1],
         [1,1,1,1,1]]
        
        \"\"\"
        if not A: return 0
        rows, cols = len(A), len(A[0])
        grids = A
        source = set()
        target = set()
        
        for i in range(rows):
            for j in range(cols):
                if A[i][j] == 1  and not source:
                    source = self.search_island(grids, i, j ,source)
                elif A[i][j] == 1 and (i,j) not in source:
                    target = self.search_island(grids, i, j, target)
                
        
        queue = collections.deque([(i, j, 0) for (i, j) in source])
        
        visited = set()
        #print(source)
        #print(target)
        
        while queue:
            (row, col, step) = queue.popleft()
            
            for (dr, dc) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                r = row + dr
                c = col + dc
                if (r, c) in target:
                    return step
            
                if 0 <= r < len(grids) and 0 <= c < len(grids[0]) and grids[r][c] == 0\\
           and (r, c) not in visited:
                    visited.add((r, c))
                    queue.append((r, c, step + 1))
                
    def search_island(self, grids, row, col, visited):
        visited.add((row, col))
        
        for (dr, dc) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            r = row + dr
            c = col + dc
            if self.is_valid(grids, r, c, visited):
                visited.add((r, c))
                self.search_island(grids, r, c, visited)
        
        return visited

    def is_valid(self, grids, row, col, visited):
        if 0 <= row < len(grids) and 0 <= col < len(grids[0]) and grids[row][col] == 1\\
           and (row, col) not in visited:
            return True
        return False
