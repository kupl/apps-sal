class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return -1
        if grid[0][0] == 1:
            queue = [(0, 0, 1, 0)]
            visited = set([(0, 0, 1)])
        else:
            queue = [(0, 0, 0, 0)]
            visited = set([(0, 0, 0)])
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue != []:
            current = queue.pop(0)
            if current[0] == len(grid) - 1 and current[1] == len(grid[0]) - 1:
                return current[3]
            for d in direction:
                n = (current[0] + d[0], current[1] + d[1])
                if 0 <= n[0] < len(grid) and 0 <= n[1] < len(grid[0]):
                    blocks = current[2]
                    if grid[n[0]][n[1]] == 1:
                        blocks += 1
                    if blocks <= k and (n[0], n[1], blocks) not in visited:
                        queue.append((n[0], n[1], blocks, current[3] + 1))
                        visited.add((n[0], n[1], blocks))
        return -1
