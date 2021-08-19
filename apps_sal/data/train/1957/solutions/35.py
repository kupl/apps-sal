class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if not grid:
            return -1
        (m, n, direction) = (len(grid), len(grid[0]), [[0, 1], [0, -1], [1, 0], [-1, 0]])
        visited = [[[False] * (k + 1) for _ in range(n)] for _ in range(m)]
        visited[0][0][0] = True
        (count, queue) = (0, deque([[0, 0, 0]]))
        while len(queue) > 0:
            size = len(queue)
            for i in range(size):
                cur = queue.popleft()
                if cur[0] == m - 1 and cur[1] == n - 1:
                    return count
                for d in direction:
                    (r, c, tmpK) = (cur[0] + d[0], cur[1] + d[1], cur[2])
                    if r >= 0 and c >= 0 and (r < m) and (c < n):
                        if grid[r][c] == 1:
                            tmpK += 1
                        if tmpK <= k and (not visited[r][c][tmpK]):
                            visited[r][c][tmpK] = True
                            queue.append([r, c, tmpK])
            count += 1
        return -1
