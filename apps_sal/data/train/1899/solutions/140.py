class Solution:

    def shortestBridge(self, A: List[List[int]]) -> int:
        (R, C) = (len(A), len(A[0]))
        done = set()

        def dfs(x, y, seen, R, C):
            if A[x][y] == 0:
                return
            seen.add((x, y))
            for (nr, nc) in ((x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)):
                if 0 <= nr < R and 0 <= nc < C and (A[nr][nc] == 1) and ((nr, nc) not in seen) and ((nr, nc) not in done):
                    dfs(nr, nc, seen, R, C)
        islands = []
        for (r, row) in enumerate(A):
            for (c, col) in enumerate(row):
                if col and (r, c) not in done:
                    seen = set()
                    dfs(r, c, seen, R, C)
                    islands.append(seen)
                    done |= seen
        (first, second) = islands
        q = list(first)
        count = 0
        seen = set()
        while q:
            temp = []
            for (x, y) in q:
                for (nx, ny) in ((x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)):
                    if 0 <= nx < R and 0 <= ny < C and ((nx, ny) not in first) and ((nx, ny) not in seen):
                        if (nx, ny) in second:
                            return count
                        temp.append((nx, ny))
                        seen.add((nx, ny))
            count += 1
            q = temp[:]
        return 0
