class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:

        def dfs(pos, visited):
            if pos in visited or grid[pos[0]][pos[1]] == 0:
                return 0
            next_visited = visited | set([pos])
            next_pos = [(pos[0] - 1, pos[1]), (pos[0] + 1, pos[1]), (pos[0], pos[1] - 1), (pos[0], pos[1] + 1)]
            max_child = 0
            for p in next_pos:
                if -1 < p[0] < n and -1 < p[1] < m:
                    max_child = max(max_child, dfs(p, next_visited))
            return grid[pos[0]][pos[1]] + max_child
        n = len(grid)
        m = len(grid[0])
        max_gold = 0
        for i in range(n):
            for j in range(m):
                max_gold = max(max_gold, dfs((i, j), set()))
        return max_gold
