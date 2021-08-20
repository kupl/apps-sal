class Solution:

    def shortestBridge(self, A: List[List[int]]) -> int:
        r = len(A)
        c = len(A[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dist = [[float('inf') for j in range(c)] for i in range(r)]
        island1 = set()
        island2 = set()

        def dfs(x, y, island):
            island.add((x, y))
            for (i, j) in dirs:
                if 0 <= x + i < r and 0 <= y + j < c and (A[x + i][y + j] == 1) and ((x + i, y + j) not in island):
                    dfs(x + i, y + j, island)
        for i in range(r):
            for j in range(c):
                if A[i][j] == 1:
                    if len(island1) == 0:
                        dfs(i, j, island1)
                    elif (i, j) not in island1:
                        dfs(i, j, island2)
        q = collections.deque(list(island1))
        d = 1
        res = float('inf')
        while q:
            size = len(q)
            for i in range(size):
                (x, y) = q.popleft()
                for (i, j) in dirs:
                    if 0 <= x + i < r and 0 <= y + j < c:
                        if A[x + i][y + j] == 0 and d < dist[x + i][y + j]:
                            q.append((x + i, y + j))
                            dist[x + i][y + j] = d
                        if (x + i, y + j) in island2:
                            res = min(res, d - 1)
            d += 1
        return res
