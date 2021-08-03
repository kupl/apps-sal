import heapq
import sys
sys.setrecursionlimit(10**8)


class First:
    val = True


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        h, w = len(A), len(A[0])
        direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        First.val = True

        visited = [[0 for i in range(w)] for i in range(h)]

        def dfs(y, x, color):
            visited[y][x] = 1
            A[y][x] = color
            for dy, dx in direction:
                ny, nx = y + dy, x + dx
                if ny < 0 or ny >= h or nx < 0 or nx >= w:
                    continue
                if visited[ny][nx] or A[ny][nx] == 0:
                    continue
                dfs(ny, nx, color)

        for i in range(h):
            for j in range(w):
                if visited[i][j]:
                    continue
                if A[i][j]:
                    if First.val:
                        First.val = False
                        dfs(i, j, 1)
                    else:
                        dfs(i, j, 2)
                        break

        def bfs(i, j, start):
            q = [[0, i, j]]
            answer = 0
            while q:
                step, y, x = heapq.heappop(q)
                if A[y][x] and A[y][x] != start:
                    return step
                for dy, dx in direction:
                    ny, nx = y + dy, x + dx
                    if ny < 0 or ny >= h or nx < 0 or nx >= w:
                        continue
                    if visited[ny][nx] == 2:
                        continue
                    visited[ny][nx] = 2
                    if A[ny][nx]:
                        heapq.heappush(q, [step, ny, nx])
                    else:
                        heapq.heappush(q, [step + 1, ny, nx])

        result = 0
        for i in range(h):
            for j in range(w):
                if visited[i][j] == 2:
                    continue
                if A[i][j]:
                    start = A[i][j]
                    result = bfs(i, j, start)
                    break
            if result:
                break

        return result
