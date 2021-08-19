from queue import Queue


class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        q = Queue()
        q.put((0, 0, 0, 0))
        visited = {}
        mins = float('inf')
        nr = len(grid)
        nc = len(grid[0])
        while q.qsize() > 0:
            (i, j, obs, count) = q.get()
            if obs > k:
                continue
            if i == nr - 1 and j == nc - 1:
                mins = min(mins, count)
            if (i, j) not in visited or ((i, j) in visited and visited[i, j] > obs):
                visited[i, j] = obs
                for (x, y) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= x < nr and 0 <= y < nc:
                        if grid[x][y] == 1:
                            q.put((x, y, obs + 1, count + 1))
                        else:
                            q.put((x, y, obs, count + 1))
        if mins == float('inf'):
            return -1
        return mins
