class Solution:

    def shortestBridge(self, A: List[List[int]]) -> int:
        (M, N) = (len(A), len(A[0]))

        def dfs(i, j):
            A[i][j] = 2
            for (x, y) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < M and 0 <= y < N and (A[x][y] == 1):
                    dfs(x, y)
            return
        flag = 0
        for i in range(M):
            for j in range(N):
                if A[i][j] == 1:
                    flag = 1
                    break
            if flag:
                break
        dfs(i, j)
        q = collections.deque([(0, i, j) for i in range(M) for j in range(N) if A[i][j] == 1])
        seen = set([(i, j) for i in range(M) for j in range(N) if A[i][j] == 1])
        while q:
            (step, i, j) = q.popleft()
            if A[i][j] == 2:
                return step - 1
            for (x, y) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < M and 0 <= y < N and ((x, y) not in seen) and (A[x][y] in [0, 2]):
                    seen.add((x, y))
                    q.append((step + 1, x, y))
