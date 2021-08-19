class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        q = collections.deque()
        q.append((0, 0, 0, k))
        visited = {}
        if not grid:
            return -1
        (m, n) = (len(grid), len(grid[0]))
        while q:
            (x, y, d, lifeline) = q.popleft()
            if x == m - 1 and y == n - 1:
                return d
            for (i, j) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= i < m and 0 <= j < n:
                    if grid[i][j] == 1:
                        if lifeline >= 1:
                            if (i, j) in visited:
                                if visited[i, j] < lifeline - 1:
                                    q.append((i, j, d + 1, lifeline - 1))
                                    visited[i, j] = lifeline - 1
                            else:
                                q.append((i, j, d + 1, lifeline - 1))
                                visited[i, j] = lifeline - 1
                    elif (i, j) in visited:
                        if visited[i, j] < lifeline:
                            q.append((i, j, d + 1, lifeline))
                            visited[i, j] = lifeline
                    else:
                        q.append((i, j, d + 1, lifeline))
                        visited[i, j] = lifeline
        return -1
