class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # This is basically BFS on state graph
        # State is (path ending at P, k)
        # We don't need the whole path because the first path ending at P willl
        # be better than later paths ending at P with same k
        # Hence, different paths ending with same P can be collapsed to one state
        # represented by P
        rows, cols = len(grid), len(grid[0])
        if rows == 1 and cols == 1:
            return 0

        visited = set((0, 0, k))
        q = deque([(0, 0, k, 0)])
        while q:
            r, c, k_rem, d = q.popleft()
            edges = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            edges = [(x, y) for x, y in edges if x >= 0 and x < rows and y >= 0 and y < cols]
            edges = [(x, y, (k_rem - 1) if grid[x][y] == 1 else k_rem) for x, y in edges]
            edges = [edge for edge in edges if edge[2] >= 0 and edge not in visited]
            for x, y, rem in edges:
                if x == rows - 1 and y == cols - 1:
                    return d + 1
                q.append((x, y, rem, d + 1))
                visited.add((x, y, rem))
        
        return -1
