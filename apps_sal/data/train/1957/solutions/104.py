class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[[False for _ in range(k + 1)] for _ in range(n)] for _ in range(m)]

        initialK = k - grid[0][0] - grid[m - 1][n - 1]

        if initialK < 0:
            return -1
        visited[0][0][initialK] = True

        initial = ((0, 0), initialK)
        queue = [initial]
        length = 0

        while queue:
            size = len(queue)
            length += 1
            for _ in range(size):
                node, kLeft = queue.pop(0)
                x, y = node
                if kLeft >= 0 and x == m - 1 and y == n - 1:
                    return length - 1

                for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nextX = x + direction[0]
                    nextY = y + direction[1]

                    if 0 <= nextX < m and 0 <= nextY < n:
                        nextKLeft = kLeft - grid[nextX][nextY]
                        if nextKLeft < 0 or visited[nextX][nextY][nextKLeft]:
                            continue
                        else:
                            if nextX == m - 1 and nextY == n - 1:
                                return length
                            queue.append(((nextX, nextY), nextKLeft))
                            visited[nextX][nextY][nextKLeft] = True

        return -1
