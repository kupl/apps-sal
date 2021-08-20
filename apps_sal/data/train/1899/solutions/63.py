class Solution:

    def shortestBridge(self, A: List[List[int]]) -> int:
        m = len(A)
        n = len(A[0])
        visited = [[False] * n for _ in range(m)]
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        def findFirstIsland():
            for r in range(m):
                for c in range(n):
                    if A[r][c] == 1:
                        return (r, c)
        queue = deque()

        def dfs(r, c):
            if visited[r][c]:
                return
            visited[r][c] = True
            if isBoundary(r, c):
                queue.append((r, c, -1))
            for (dr, dc) in directions:
                (nr, nc) = (r + dr, c + dc)
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                if A[nr][nc] == 1 and (not visited[nr][nc]):
                    dfs(nr, nc)

        def isBoundary(r, c):
            for (dr, dc) in directions:
                (nr, nc) = (r + dr, c + dc)
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                if A[nr][nc] == 0:
                    return True
            return False
        (sr, sc) = findFirstIsland()
        dfs(sr, sc)
        visited2 = [[False] * n for _ in range(m)]
        while queue:
            (r, c, d) = queue.popleft()
            visited2[r][c] = True
            if not visited[r][c] and A[r][c] == 1:
                return d
            for (dr, dc) in directions:
                (nr, nc) = (r + dr, c + dc)
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                if not visited2[nr][nc]:
                    visited2[nr][nc] = True
                    queue.append((nr, nc, d + 1))
        return 1
