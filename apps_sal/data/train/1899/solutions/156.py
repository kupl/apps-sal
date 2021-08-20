class Solution:

    def shortestBridge(self, A: List[List[int]]) -> int:
        m = len(A)
        n = len(A[0])
        q = collections.deque([])
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    q.append((i, j))
                    newq = collections.deque([(i, j)])
                    break
            else:
                continue
            break
        while q:
            (x, y) = q.popleft()
            A[x][y] = 2
            for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                (nx, ny) = (x + dx, y + dy)
                if 0 <= nx < m and 0 <= ny < n and (A[nx][ny] == 1):
                    A[nx][ny] = 2
                    newq.append((nx, ny))
                    q.append((nx, ny))
        steps = 0
        while newq:
            newsize = len(newq)
            for _ in range(newsize):
                (x, y) = newq.popleft()
                for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    (nx, ny) = (x + dx, y + dy)
                    if nx < 0 or nx >= m or ny < 0 or (ny >= m) or (A[nx][ny] == 2):
                        continue
                    if A[nx][ny] == 1:
                        return steps
                    elif A[nx][ny] == 0:
                        A[nx][ny] = 2
                        newq.append((nx, ny))
            steps += 1
        return -1
