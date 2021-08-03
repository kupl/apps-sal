class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        row = len(grid)
        col = len(grid[0])
        queue = []
        queue.append((0, 0, k, 0))
        visited = set()
        visited.add((0, 0, k))
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            r, c, ob, step = queue.pop(0)
            if (r, c) == (row - 1, col - 1):
                return step

            if grid[r][c] == 1:
                if ob == 0:
                    continue
                else:
                    ob -= 1

            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if (nr, nc, ob) in visited:
                    continue
                if not 0 <= nr < row:
                    continue
                if not 0 <= nc < col:
                    continue

                queue.append((nr, nc, ob, step + 1))
                visited.add((nr, nc, ob))
                pass

            pass

        return -1
