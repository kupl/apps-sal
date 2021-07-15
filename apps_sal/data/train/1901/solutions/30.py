class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        return self.largestIsland_dfs(grid)
        
        
    def largestIsland_dfs(self, grid: List[List[int]]) -> int:
        \"\"\"
        * Make eavery island a unqiue index (dfs, bfs)
        * Chehck every empty cell(0) to figure out largest area
        \"\"\"
        
        def moves(row, col):
            for rm, cm in (0, 1), (1, 0), (0, -1), (-1, 0):
                nr, nc = row + rm, col + cm
                if 0 <= nr < rows and 0 <= nc < cols:
                    yield nr, nc
        
        def dfs(row, col, index) -> int:
            grid[row][col] = index
            cur_size = 1
            for nr, nc in moves(row, col):
                if grid[nr][nc] != 1:
                    continue
                cur_size += dfs(nr, nc, index)
            return cur_size
        
        rows, cols = len(grid), len(grid[0])
        index = 2
        island_to_size = defaultdict(int)
        # island_to_size = {0:0} # edge case: input [[0,0],[0,0]]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 1:
                    continue
                size = dfs(r, c, index)
                island_to_size[index] = size
                index += 1
                
        # edge case: [[1,1], [1, 1]] or [[1]]
        # max_size = max(island_to_size.values())
        max_size = max(island_to_size.values()) if island_to_size else 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    continue
                islands = set([grid[nr][nc] for nr, nc in moves(r, c)])
                cur_size = sum(island_to_size[idx] for idx in islands) + 1
                max_size = max(max_size, cur_size)
                
        return max_size
                

        
