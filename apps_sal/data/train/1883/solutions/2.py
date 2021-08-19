class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        count = 0
        visited = set()

        def dfs(i: int, j: int):
            nonlocal count
            nonlocal num_empty

            if grid[i][j] == -1 or (i, j) in visited:
                return
            # + 1 to account for starting position
            elif grid[i][j] == 2 and len(visited) == num_empty + 1:
                count += 1
                return
            else:
                visited.add((i, j))

                if i > 0:
                    dfs(i - 1, j)
                if j > 0:
                    dfs(i, j - 1)
                if i < len(grid) - 1:
                    dfs(i + 1, j)
                if j < len(grid[0]) - 1:
                    dfs(i, j + 1)

                visited.remove((i, j))

        # 1) Find starting position
        # 2) Count all empty squares
        start_i = start_j = None
        num_empty = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    start_i, start_j = i, j
                elif grid[i][j] == 0:
                    num_empty += 1

        dfs(start_i, start_j)
        return count
