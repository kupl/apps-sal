import queue


def isOK(x, y, m, n):
    return x >= 0 and y >= 0 and x < m and y < n


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        m = len(A)
        n = len(A[0])

        visited = [[False for _ in range(n)] for _ in range(m)]

        def dfs(start, island):
            x, y = start
            island.append(start)
            visited[x][y] = True
            xRows = [0, 0, -1, 1]
            yCols = [-1, 1, 0, 0]
            for i in range(4):
                new_x = x + xRows[i]
                new_y = y + yCols[i]
                if isOK(new_x, new_y, m, n) and not visited[new_x][new_y] and A[new_x][new_y] == 1:
                    dfs((new_x, new_y), island)

        islands = []
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and A[i][j] == 1:
                    island = []
                    dfs((i, j), island)
                    islands.append(island)

        island1 = islands[0]
        island2 = islands[1]

        visited = [[False for _ in range(n)] for _ in range(m)]

        def bfs(source_island, target_island, visited):
            q = queue.Queue()

            for start in source_island:
                x, y = start
                q.put((x, y, 0))
            cnt = 0

            while q.qsize() > 0:
                start = q.get()
                x, y, w = start
                xRows = [0, 0, -1, 1]
                yCols = [-1, 1, 0, 0]
                for i in range(4):
                    new_x = x + xRows[i]
                    new_y = y + yCols[i]
                    if isOK(new_x, new_y, m, n) and not visited[new_x][new_y]:
                        if (new_x, new_y) in target_island:
                            return w + 1

                        visited[new_x][new_y] = True
                        q.put((new_x, new_y, w + 1))

        return bfs(island1, island2, visited) - 1
