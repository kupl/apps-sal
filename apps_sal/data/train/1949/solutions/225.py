class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        deltas = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def explore(y: int, x: int, score=0, visited=None) -> int:
            if not visited:
                visited = set()

            if y < 0 or y >= num_rows or x < 0 or x >= num_cols:
                return score
            if grid[y][x] == 0 or (y, x) in visited:
                return score

            score += grid[y][x]
            visited = set([*visited, (y, x)])

            best = score
            for dy, dx in deltas:
                best = max(best, explore(y + dy, x + dx, score, visited))
            return best

        best = 0
        for y in range(num_rows):
            for x in range(num_cols):
                best = max(best, explore(y, x))
        return best
