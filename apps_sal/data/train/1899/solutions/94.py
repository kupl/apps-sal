class Solution:

    def shortestBridge(self, A: List[List[int]]) -> int:
        m = len(A)
        n = len(A[0])
        visited = collections.deque()
        flag = False
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    A[i][j] = 2
                    visited = self.search(A, i, j, visited)
                    flag = True
                    break
            if flag == True:
                break
        steps = 0
        vis = collections.deque(visited)
        while visited:
            size = len(visited)
            for i in range(size):
                (row, col) = visited.popleft()
                dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for d in dirs:
                    newrow = row + d[0]
                    newcol = col + d[1]
                    if 0 <= newrow < len(A) and 0 <= newcol < len(A[0]) and (A[newrow][newcol] == 1):
                        return steps
                    elif 0 <= newrow < len(A) and 0 <= newcol < len(A[0]) and (A[newrow][newcol] == 0) and ((newrow, newcol) not in vis):
                        A[newrow][newcol] = 2
                        visited.append((newrow, newcol))
                        vis.append((newrow, newcol))
            steps += 1
        return -1

    def search(self, A, i, j, visited):
        q = collections.deque()
        q.append((i, j))
        visited.append((i, j))
        while q:
            size = len(q)
            for i in range(size):
                (r, c) = q.popleft()
                dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for d in dirs:
                    newr = r + d[0]
                    newc = c + d[1]
                    if 0 <= newr < len(A) and 0 <= newc < len(A[0]) and (A[newr][newc] == 1) and ((newr, newc) not in visited):
                        A[newr][newc] = 2
                        q.append((newr, newc))
                        visited.append((newr, newc))
        return visited
