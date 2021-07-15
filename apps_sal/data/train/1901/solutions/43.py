from collections import defaultdict
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def dfs(m, n, c_id):
            nonlocal grid, c_dict
            stack = [(m, n)]
            size = 1
            while stack:
                i, j = stack.pop()
                children = [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)]
                for x, y in children:
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                        grid[x][y] = c_id
                        size += 1
                        stack.append((x, y))
            c_dict[c_id] = size
        c_id = 1
        c_dict = defaultdict(int)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    c_id += 1
                    grid[i][j] = c_id
                    dfs(i, j, c_id)
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0: continue
                children = [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)]
                n_c = set()
                for x, y in children:
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] > 0:
                        n_c.add(grid[x][y])
                result = max(result, sum([c_dict[c] for c in n_c]) + 1)
        return result if result > 0 else len(grid) * len(grid[0])
