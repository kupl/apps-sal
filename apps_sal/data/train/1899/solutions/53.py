class Solution:

    def shortestBridge(self, A: List[List[int]]) -> int:
        (i1, i2) = ([], [])
        m = len(A)
        n = len(A[0])
        vis = [[False for _ in range(n)] for _ in range(m)]

        def check(x, y):
            return x >= 0 and x < m and (y >= 0) and (y < n)
        dx = [0, -1, 0, 1]
        dy = [1, 0, -1, 0]

        def dfs(p_x, p_y, i):
            vis[p_x][p_y] = True
            i.append((p_x, p_y))
            for j in range(4):
                (c_x, c_y) = (p_x + dx[j], p_y + dy[j])
                if check(c_x, c_y) and (not vis[c_x][c_y]):
                    if A[c_x][c_y]:
                        dfs(c_x, c_y, i)
        conn = 0
        for i in range(m):
            for j in range(n):
                if not vis[i][j] and A[i][j]:
                    if conn == 0:
                        dfs(i, j, i1)
                    elif conn == 1:
                        dfs(i, j, i2)
                    else:
                        conn += 1
                        break
                    conn += 1
        q = deque()
        d = [[float('inf') for _ in range(n)] for _ in range(m)]
        for v in i1:
            q.append(v)
            d[v[0]][v[1]] = 0
        ans = float('inf')
        while q:
            (s_x, s_y) = (q[0][0], q[0][1])
            q.popleft()
            for i in range(4):
                (c_x, c_y) = (s_x + dx[i], s_y + dy[i])
                if check(c_x, c_y):
                    if d[c_x][c_y] > d[s_x][s_y] + 1:
                        d[c_x][c_y] = d[s_x][s_y] + 1
                        q.append((c_x, c_y))
                        if vis[c_x][c_y]:
                            ans = min(ans, d[c_x][c_y] - 1)
        return ans
