class Solution:

    def shortestBridge(self, A: List[List[int]]) -> int:

        def dfs(A, i, j):
            if i < 0 or j < 0 or i > len(A) - 1 or (j > len(A[0]) - 1):
                return
            if visited[i][j] or A[i][j] == 0:
                return
            visited[i][j] = True
            queue.append((i, j))
            for k in range(4):
                rr = i + rowVector[k]
                cc = j + colVector[k]
                dfs(A, rr, cc)
        visited = [[False for i in range(len(A[0]))] for j in range(len(A))]
        rowVector = [1, -1, 0, 0]
        colVector = [0, 0, 1, -1]
        queue = []
        found = False
        for i in range(len(A)):
            if found:
                break
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    dfs(A, i, j)
                    found = True
                    break
        count = 0
        while queue:
            subQ = []
            while queue:
                temp = queue.pop(0)
                for k in range(4):
                    i = temp[0] + rowVector[k]
                    j = temp[1] + colVector[k]
                    if i < 0 or j < 0 or i > len(A) - 1 or (j > len(A[0]) - 1) or visited[i][j]:
                        continue
                    if A[i][j] == 1:
                        return count
                    subQ.append((i, j))
                    visited[i][j] = True
            queue = subQ
            count += 1
        return -1
