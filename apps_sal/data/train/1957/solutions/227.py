class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        queue = deque([[0, 0, 0, 0]])
        n, m = len(grid), len(grid[0])
        minObs = [0] * n
        move = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        for i in range(n):
            minObs[i] = [1e9] * m

        while len(queue):
            r, c, obs, steps = queue.popleft()

            if r == n - 1 and c == m - 1:
                return steps

            for mR, mC in move:
                nextR = r + mR
                nextC = c + mC

                if 0 <= nextR < n and 0 <= nextC < m and obs + grid[nextR][nextC] <= k and obs + grid[nextR][nextC] < minObs[nextR][nextC]:
                    minObs[nextR][nextC] = obs + grid[nextR][nextC]
                    queue.append([nextR, nextC, obs + grid[nextR][nextC], steps + 1])

        return -1
