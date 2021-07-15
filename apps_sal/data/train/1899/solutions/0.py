class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = deque()
        boundary = set()
        found = False
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    A[i][j] = 2
                    queue.append((i, j))
                    while queue:
                        ci, cj = queue.popleft()
                        for di, dj in dirs:
                            ni, nj = ci + di, cj + dj
                            if 0 <= ni < m and 0 <= nj < n:
                                if A[ni][nj] == 1:
                                    A[ni][nj] = 2
                                    queue.append((ni, nj))
                                elif A[ni][nj] == 0:
                                    boundary.add((ci, cj))
                    found = True
                    break
            if found:
                break
                
        queue = deque(boundary)
        steps = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n:
                        if A[ni][nj] == 0:
                            A[ni][nj] = 2
                            queue.append((ni, nj))
                        elif A[ni][nj] == 1:
                            return steps
            steps += 1
