class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:

        def BFS(r, c):
            nonlocal best, best_path, R, C, grid
            if grid[r][c] > best:
                best = grid[r][c]
                best_path = set([(r, c)])
            q = [(grid[r][c], r, c, set([(r, c)]))]
            while q:
                next_level = []
                for (t, r, c, p) in q:
                    for (i, j) in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                        if 0 <= i < R and 0 <= j < C and grid[i][j]:
                            if (i, j) not in p:
                                next_level.append((t + grid[i][j], i, j, p | set([(i, j)])))
                                if t + grid[i][j] > best:
                                    best = t + grid[i][j]
                                    best_path = p | set([(i, j)])
                q = next_level
        (R, C) = (len(grid), len(grid[0]))
        best = 0
        best_path = set()
        for r in range(R):
            for c in range(C):
                if grid[r][c]:
                    if (r, c) not in best_path:
                        BFS(r, c)
        return best
