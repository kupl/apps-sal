class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = [(0, 0, 0)]
        steps = 0
        while queue:
            new_q = []
            for (x, y, r) in queue:
                if x == len(grid) - 1 and y == len(grid[0]) - 1:
                    return steps
                for (ix, iy) in directions:
                    xx = x + ix
                    yy = y + iy
                    if xx >= 0 and xx < len(grid) and (yy >= 0) and (yy < len(grid[0])):
                        rr = r + (1 if grid[xx][yy] == 1 else 0)
                        if (xx, yy, rr) not in visited and rr <= k:
                            visited.add((xx, yy, rr))
                            new_q.append((xx, yy, rr))
            steps += 1
            queue = new_q
        return -1
