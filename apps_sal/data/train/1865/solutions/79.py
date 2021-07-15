class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        player, box = [0, 0], [0, 0]
        
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 'B':
                    box = [i, j]
                elif grid[i][j] == 'S':
                    player = [i, j]
        
        i, j = box
        x, y = player
        q = collections.deque()
        q.append((i, j, x, y))  # i, j is where the box is, x, y is where the player is
        visited = set()
        visited.add((i, j, x, y))
        
        step = 0
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while q:
            size = len(q)
            for _ in range(size):
                i, j, x, y = q.popleft()
                if grid[i][j] == 'T':
                    return step
                
                for di, dj in dirs:
                    i2 = i + di
                    j2 = j + dj
                    if i2 < 0 or i2 >= self.m or j2 < 0 or j2 >= self.n or (i2, j2, i, j) in visited or grid[i2][j2] == '#' or not self.helper(grid, x, y, i, j, i - di, j - dj):
                        continue
                
                    q.append((i2, j2, i, j))
                    visited.add((i2, j2, i, j))
            step += 1
        
        return -1
    
    def helper(self, grid, x, y, bi, bj, i, j):
        # check if the player can go from x, y to i, j
        visited = set()
        return self.has_path(grid, x, y, bi, bj, i, j, visited)
    
    def has_path(self, grid, x, y, bi, bj, i, j, visited):
        # check if the player can go from x, y to i, j
        if x < 0 or x >= self.m or y < 0 or y >= self.n or (x == bi and y == bj) or grid[x][y] == '#' or (x, y) in visited:
            return False
        
        if x == i and y == j:
            return True
        
        visited.add((x, y))
        return self.has_path(grid, x - 1, y, bi, bj, i, j, visited) or self.has_path(grid, x + 1, y, bi, bj, i, j, visited) or self.has_path(grid, x, y + 1, bi, bj, i, j, visited) or self.has_path(grid, x, y - 1, bi, bj, i, j, visited)
        
        

