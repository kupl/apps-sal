class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])

        def neighbors(r, c):
            result = []
            for newR, newC in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= newR < N and 0 <= newC < M:
                    result.append((newR, newC))
            return result

        def dfs(r, c, index):
            ans = 1
            grid[r][c] = index
            for newR, newC in neighbors(r, c):
                if grid[newR][newC] == 1:
                    ans += dfs(newR, newC, index)
            return ans

        area = {}
        index = 2
        for r in range(N):
            for c in range(M):
                if grid[r][c] == 1:
                    area[index] = dfs(r, c, index)
                    index += 1

        ans = max(area.values() or [0])
        for r in range(N):
            for c in range(M):
                if grid[r][c] == 0:
                    seen = {grid[newR][newC] for newR, newC in neighbors(r, c) if grid[newR][newC] > 1}
                    ans = max(ans, 1 + sum(area[i] for i in seen))
        return ans
