class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        def neighbors(r, c):
            for nr, nc in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    yield nr, nc

        def dfs(r, c, island_num):
            island_area = 1
            grid[r][c] = island_num
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    island_area += dfs(nr, nc, island_num)
            return island_area

        area = {}
        island_num = 2

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    area[island_num] = dfs(r, c, island_num)
                    island_num += 1

        ans = max(area.values() or [0])

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    neighboring_islands = set()
                    for nr, nc in neighbors(r, c):
                        if grid[nr][nc] > 1:
                            neighboring_islands.add(grid[nr][nc])

                    ans = max(ans, 1 + sum(area[i] for i in neighboring_islands))
        return ans
