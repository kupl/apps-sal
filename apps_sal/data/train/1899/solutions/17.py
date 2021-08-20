class Solution:

    def shortestBridge(self, A: List[List[int]]) -> int:
        q = []
        r = len(A)
        c = len(A[0])
        result = float('inf')
        seen = [[False] * c for _ in range(r)]
        found = False
        for i in range(r):
            if found:
                break
            for j in range(c):
                if A[i][j] == 1:
                    q = self.neighbors(i, j, A, seen, r, c)
                    found = True
                    break
        while q:
            (x, y, dis) = q.pop(0)
            for (d1, d2) in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                (n_x, n_y) = (d1 + x, d2 + y)
                if 0 <= n_x < r and 0 <= n_y < c and (not seen[n_x][n_y]):
                    if A[n_x][n_y] == 1:
                        result = min(result, dis)
                    q.append((n_x, n_y, dis + 1))
                    seen[n_x][n_y] = True
        return result

    def neighbors(self, i, j, A, seen, r, c):
        q = [(i, j)]
        seen[i][j] = True
        ls = []
        while q:
            (x, y) = q.pop(0)
            ls.append((x, y, 0))
            for (d1, d2) in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                (n_x, n_y) = (d1 + x, d2 + y)
                if 0 <= n_x < r and 0 <= n_y < c and (A[n_x][n_y] == 1) and (not seen[n_x][n_y]):
                    q.append((n_x, n_y))
                    seen[n_x][n_y] = True
        return ls
