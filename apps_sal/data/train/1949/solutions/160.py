class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def sorround(curr):
            posts = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for i in posts:
                ii = i[0] + curr[0]
                jj = i[1] + curr[1]
                if(ii < len(grid) and ii >= 0 and jj >= 0 and jj < len(grid[0]) and grid[ii][jj] != 0):
                    yield (ii, jj)

        def depth_first_search(cur):
            cur_sum = grid[cur[0]][cur[1]]
            ans = 0
            for i in sorround(cur):
                if((i not in visited) or (visited[i] == False)):
                    visited[i] = True
                    mx = depth_first_search(i)
                    ans = max(ans, mx)
                    visited[i] = False
            return cur_sum + ans
        cans = 0
        visited = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] != 0):
                    visited[(i, j)] = True
                    cs = depth_first_search((i, j))
                    cans = max(cs, cans)
                    visited[(i, j)] = False
        return cans
