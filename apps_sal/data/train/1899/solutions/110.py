class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        
        R = len(A)
        C = len(A[0])
        
        chk = [[0] * C for _ in range(R)]
        q = collections.deque()
        move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        flag = False
        
        #find the first land
        for i in range(R):
            if flag: break
            for j in range(C):
                if A[i][j] == 1:
                    self.dfs(i, j, A, chk, q)
                    flag = True
                    break
        
        res = 0
        
        while q:
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()
            
                for m in move:
                    x, y = i + m[0], j + m[1]
                    if 0 <= x < R and 0 <= y < C:
                        chk[x][y] = 1
                        if A[x][y] == 1:
                            return res
                        elif A[x][y] == 0:
                            A[x][y] = 2
                            q.append((x, y))
                        else:
                            continue
            res += 1
            
        return res
        
    def dfs(self, i, j, A, chk, q):
        # print(i, j)
        if chk[i][j] == 1:
            return
        
        chk[i][j] = 1
        
        R = len(A)
        C = len(A[0])
        move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        if A[i][j] == 1:
            q.append((i, j))
            A[i][j] = 2
            for m in move:
                x = i + m[0]
                y = j + m[1]
                
                if 0 <= x < R and 0 <= y < C:
                    self.dfs(x, y, A, chk, q)

