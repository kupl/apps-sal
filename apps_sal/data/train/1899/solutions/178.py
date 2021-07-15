class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        
        def dfs(i, j, A, visited):
            m = len(A)
            n = len(A[0])
            if 0<=i<m and 0<=j<n and A[i][j] == 1 and (i, j) not in visited:
                visited.add((i,j))
                dfs(i+1, j, A, visited)
                dfs(i-1, j, A, visited)
                dfs(i, j+1, A, visited)
                dfs(i, j-1, A, visited)

        m = len(A)
        n = len(A[0])
        find = False
        visited = set()
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    find = True
                    dfs(i, j, A, visited)
                    break
            if find:
                break
        
        # print(visited)
        
        visited_zero = set()
        queue = []
        for i, j in visited:
            for _i, _j in [[0,1],[1,0],[-1,0],[0,-1]]:
                if 0<=i+_i<m and 0<=j+_j<n and (i+_i, j+_j) not in visited:
                    assert A[i+_i][j+_j] == 0
                    visited_zero.add((i+_i, j+_j))
                    queue.append((i+_i, j+_j, 1))
        
        # print(queue)
        
        res = 0
        find = False
        while not find:
            i, j, dist = queue.pop(0)
            for _i, _j in [[0,1],[1,0],[-1,0],[0,-1]]:
                if 0<=i+_i<m and 0<=j+_j<n and (i+_i, j+_j) not in visited_zero and (i+_i, j+_j) not in visited:
                    if A[i+_i][j+_j] == 0:
                        visited_zero.add((i+_i, j+_j))
                        queue.append((i+_i, j+_j, dist+1))
                    else:
                        find = True
                        res = dist
        return res
