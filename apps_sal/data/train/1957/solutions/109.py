class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        queue = deque()
        visited = set()
        queue.append((0, 0, k, 0))
        while queue:
            (i, j, r, l) = queue.popleft()
            if (i, j, r) in visited:
                continue
            visited.add((i, j, r))
            if grid[i][j] == 1:
                r -= 1
            if r < 0:
                continue
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return l
            neighbors = {(1, 0), (0, 1), (-1, 0), (0, -1)}
            for n in neighbors:
                (x, y) = (i + n[0], j + n[1])
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                    queue.append((x, y, r, l + 1))
        return -1
