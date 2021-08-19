class Solution():
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(i: int, j: int, sum_so_far: int, seen: set) -> int:
            if i < 0 or i >= m or j < 0 or j >= n or not grid[i][j] or (i, j) in seen:
                return sum_so_far

            seen.add((i, j))
            sum_so_far += grid[i][j]
            mx = 0
            for x, y in ((i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)):
                mx = max(dfs(x, y, sum_so_far, seen), mx)
            seen.discard((i, j))
            return mx

        m, n = len(grid), len(grid[0])
        all_gold_path = 0
        for row in range(m):
            for col in range(n):
                all_gold_path = max(all_gold_path, dfs(row, col, 0, set()))
        # print(all_gold_path)
        return all_gold_path
        # return max(dfs(i, j, 0, set()) for j in range(n) for i in range(m))
# class Solution:
#     def getMaximumGold(self, grid: List[List[int]]) -> int:
#         def findMaxGold(r: int, c: int) -> int:
#             if r < 0 or r == m or c < 0 or c == n or grid[r][c] == 0: return 0
#             origin = grid[r][c]
#             grid[r][c] = 0  # mark as visited
#             maxGold = 0
#             for nr, nc in ((r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)):
#                 maxGold = max(findMaxGold(nr, nc), maxGold)
#             grid[r][c] = origin  # backtrack
#             return maxGold + origin

#         m, n = len(grid), len(grid[0])
#         return max(findMaxGold(r, c) for c in range(n) for r in range(m))

# class Solution:
#     def getMaximumGold(self, grid: List[List[int]]) -> int:
#         #2D array
#         #0 means no gold
#         #some_num > 0 means there is gold
#         #Return the max gold you can collect with these conditions

#         #1) IN w.e cell you are collect ALL the gold in that cell
#         #From you position move U D L R
#         #You can't VISIT the same cell more than once.
#         #You can start and stop collecting gold from ANY position in the grid that has some gold.
#         visited = set()
#         max_path = [0]
#         row_len = len(grid)
#         col_len = len(grid[0])

#         def gold_finder(cur_row, cur_col, visited, path_so_far):
#             #Can't visit area that is zero.

#             #Out of boundary check
#             if cur_row < 0 or cur_row >= row_len or cur_col < 0 or cur_col >= col_len or grid[cur_row][cur_col] == 0:
#                 max_path[0] = max(max_path[0], sum(path_so_far))
#                 return
#             # if grid[cur_row][cur_col] == 0:
#             #     return

#             #If visited we can't visit you again.
#             if (cur_row, cur_col) in visited:
#                 return

#             visited.add((cur_row,cur_col))
#             gold_finder(cur_row + 1, cur_col, visited, path_so_far + [grid[cur_row][cur_col]])
#             gold_finder(cur_row - 1, cur_col, visited, path_so_far + [grid[cur_row][cur_col]])
#             gold_finder(cur_row , cur_col + 1, visited, path_so_far + [grid[cur_row][cur_col]])
#             gold_finder(cur_row, cur_col - 1, visited, path_so_far + [grid[cur_row][cur_col]])
#             visited.remove((cur_row,cur_col))

#             return

#         for row in range(row_len):
#             for col in range(col_len):
#                 gold_finder(row, col, visited, [])


#         # print('before', max_path)
#         # max_path = max(max_path)
#         # print('after', max_path)
#         return max_path[0]
