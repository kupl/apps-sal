class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        if not A:
            return 0
        m = len(A)
        n = len(A[0])

        def getnei(i, j):
            xy = []
            if i > 0:
                xy.append((i - 1, j))
            if j > 0:
                xy.append((i, j - 1))
            if i < m - 1:
                xy.append((i + 1, j))
            if j < m - 1:
                xy.append((i, j + 1))
            return xy

        def dfs1(i, j):
            if A[i][j] != 1:
                return
            A[i][j] = -1
            for x, y in getnei(i, j):
                dfs1(x, y)

        def bfs(i, j, dist_map, thresh):
            seen = set()
            q = collections.deque()
            q.append((i, j, 0))
            done = False
            while q and not done:
                (ii, jj, depth) = q.popleft()
                if depth > thresh:
                    done = True
                    break

                for x, y in getnei(ii, jj):
                    if (x, y) in dist_map and dist_map[(x, y)] < depth:
                        continue

                    if A[x][y] == -1:
                        thresh = min(depth, thresh)
                        done = True
                        break
                    elif A[x][y] == 0:
                        if (x, y) in seen:
                            continue
                        seen.add((x, y))
                        q.append((x, y, depth + 1))

            return thresh

        ans = math.inf
        is_second = False
        dist_map = {}
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    if not is_second:
                        dfs1(i, j)
                        is_second = True
                    else:
                        ans = min(ans, bfs(i, j, dist_map, ans))

        return ans
