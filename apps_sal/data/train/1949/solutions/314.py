class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        golds = [(i, j) for i in range(rows) for j in range(cols) if grid[i][j] != 0]
        visited = {}

        def dfs(curr_r, curr_c, curr_gold):
            tmp = []
            for move in moves:
                new_r, new_c = curr_r + move[0], curr_c + move[1]

                if new_r >= 0 and new_r < rows and new_c >= 0 and new_c < cols and grid[new_r][new_c] != 0 and (new_r, new_c) not in visited:
                    visited[(new_r, new_c)] = 1
                    tmp.append(dfs(new_r, new_c, curr_gold + grid[new_r][new_c]))
                    del visited[(new_r, new_c)]

            if len(tmp) != 0:
                return max(tmp)
            else:
                return curr_gold

        res = float('-inf')
        for g in golds:
            i, j = g
            visited[(i, j)] = 1
            tmp = dfs(i, j, grid[i][j])
            res = max(res, tmp)
            del visited[(i, j)]
        return res
