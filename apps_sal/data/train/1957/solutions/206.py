class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        q = []
        visited = set()
        q.append([0, 0, k - grid[0][0], 0])
        visited.add((0, 0, k - grid[0][0]))
        step = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        n = len(grid)
        m = len(grid[0])

        if (n == 1) and (m == 1) and (q[0][2] >= 0):
            return 0

        while (q):
            now = q.pop(0)
            # print(now)
            # print(visited)
            for i in range(4):
                new = [now[0] + step[i][0], now[1] + step[i][1], 0, now[3] + 1]
                if (0 <= new[0] < n) and (0 <= new[1] < m):
                    i = new[0]
                    j = new[1]
                    new[2] = now[2] - grid[i][j]
                    # if (i == n - 1) and (j == m - 1):
                    #     print(new)
                    #     print(visited)
                    if (new[2] >= 0) and ((tuple(new[:3])) not in visited):
                        if (i == n - 1) and (j == m - 1):
                            return new[3]
                        q.append(new)
                        visited.add(tuple(new[:3]))
        return -1
