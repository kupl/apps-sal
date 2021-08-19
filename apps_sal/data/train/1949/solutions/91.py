class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        di = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    v = self.bfs(grid, i, j, di)
                    # print(f'{v=} | {i=} | {j=}')
                    ans = max(ans, v)
        return ans

    def bfs(self, A, r, c, di):
        q = collections.deque([[r, c, A[r][c], {(r, c)}]])
        mx = 0
        while q:
            x, y, n, seen = q.popleft()
            seen.add((x, y))
            mx = max(mx, n)
            # print(f'{r=} | {c=} | {x=} | {y=} | {n=} | {mx=} | {seen=}')
            for i, j in di:
                nx, ny = x + i, y + j
                if (nx, ny) not in seen and 0 <= nx < len(A) and 0 <= ny < len(A[0]) and A[nx][ny] != 0:
                    q.append([nx, ny, n + A[nx][ny], seen.copy()])
        return mx
