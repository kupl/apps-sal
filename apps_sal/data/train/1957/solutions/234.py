class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        (m, n) = (len(grid), len(grid[0]))
        q = collections.deque()
        q.append((0, 0, 0, 0))
        explored = {(0, 0): 0}
        ans = 1 << 31 - 1
        while q:
            (i, j, obs, dist) = q.popleft()
            if i == m - 1 and j == n - 1:
                ans = min(ans, dist)
            for (di, dj) in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= di < m and 0 <= dj < n:
                    if ((di, dj) not in explored or explored[di, dj] > obs + grid[di][dj]) and obs + grid[di][dj] <= k:
                        explored[di, dj] = obs + grid[di][dj]
                        q.append((di, dj, obs + grid[di][dj], dist + 1))
        return ans if ans < m * n else -1
