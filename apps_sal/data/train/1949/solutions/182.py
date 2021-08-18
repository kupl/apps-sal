class Solution():
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(i: int, j: int, sum_so_far: int, seen: set) -> int:
            if i < 0 or i >= m or j < 0 or j >= n or not grid[i][j] or (i, j) in seen:
                return sum_so_far

            seen.add((i, j))
            sum_so_far += grid[i][j]
            max_all = 0
            for x, y in ((i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)):
                max_all = max(dfs(x, y, sum_so_far, seen), max_all)
            seen.discard((i, j))
            return max_all

        m, n = len(grid), len(grid[0])
        all_gold_path = 0
        for row in range(m):
            for col in range(n):
                all_gold_path = max(all_gold_path, dfs(row, col, 0, set()))
        return all_gold_path


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        visited = set()
        max_path = [0]
        row_len = len(grid)
        col_len = len(grid[0])

        def gold_finder(cur_row, cur_col, visited, path_so_far):

            if cur_row < 0 or cur_row >= row_len or cur_col < 0 or cur_col >= col_len or grid[cur_row][cur_col] == 0:
                max_path[0] = max(max_path[0], sum(path_so_far))
                return

            if (cur_row, cur_col) in visited:
                return

            visited.add((cur_row, cur_col))
            gold_finder(cur_row + 1, cur_col, visited, path_so_far + [grid[cur_row][cur_col]])
            gold_finder(cur_row - 1, cur_col, visited, path_so_far + [grid[cur_row][cur_col]])
            gold_finder(cur_row, cur_col + 1, visited, path_so_far + [grid[cur_row][cur_col]])
            gold_finder(cur_row, cur_col - 1, visited, path_so_far + [grid[cur_row][cur_col]])
            visited.remove((cur_row, cur_col))

            return

        for row in range(row_len):
            for col in range(col_len):
                gold_finder(row, col, visited, [])

        return max_path[0]
