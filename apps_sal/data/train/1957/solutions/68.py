class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        q = collections.deque([(0, 0, 0, k)])
        vis = set([(0, 0, k)])
        while q:
            (x, y, s, r) = q.popleft()
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return s
            for (i, j) in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                    if grid[i][j] == 1 and r > 0 and ((i, j, r - 1) not in vis):
                        vis.add((i, j, r - 1))
                        q.append((i, j, s + 1, r - 1))
                    if grid[i][j] == 0 and (i, j, r) not in vis:
                        vis.add((i, j, r))
                        q.append((i, j, s + 1, r))
        return -1
