class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        start = (0, 0, k)
        queue = collections.deque([(0, start)])
        visited = set([start])
        while queue:
            steps, (i, j, k) = queue.popleft()
            if i == m-1 and j == n-1:
                return steps
            for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n:
                    state = (x, y, k-grid[x][y])
                    if state not in visited and state[2] >= 0:
                        queue.append((steps+1, state))
                        visited.add(state)
        return -1
