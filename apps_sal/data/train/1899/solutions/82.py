'''Idea is straightforward.
We get root of first island from \"first\" function
We dfs root and add indexes of the island to bfs (all indexes of island 1)
We bfs and expand the first island in other words
Finally return step number when facing other island
Note: This can also be done with referenced array if you don't want to modify A.'''


class Solution:
    def shortestBridge(self, A):
        def dfs(i, j):
            if (i, j) not in seen:
                seen.append((i, j))
                A[i][j] = -1
                bfs.append((i, j))
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < n and 0 <= y < n and A[x][y] == 1:
                        dfs(x, y)

        def first():
            for i in range(n):
                for j in range(n):
                    if A[i][j]:
                        return i, j

        n, step, bfs = len(A), 0, []
        seen = []
        i, j = first()
        dfs(i, j)

        while bfs:
            new = []
            for i, j in bfs:
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < n and 0 <= y < n:
                        if A[x][y] == 1:
                            return step
                        elif not A[x][y]:
                            A[x][y] = -1
                            new.append((x, y))
            step += 1
            bfs = new
