class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        row_len = len(A)
        col_len = len(A[0])
        
        def neighbour(r, c):
            for i , j in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
                if 0 <= i < row_len and 0 <= j < col_len:
                    yield i, j
        
        def helper(A, r, c, queue):
            if not (0 <= r < row_len and 0 <= c <col_len) or A[r][c] == 0 or A[r][c] == 2:
                return
            A[r][c] = 2
            queue.append((r, c))
            for i, j in neighbour(r, c):
                helper(A, i, j, queue)
                    
                    
        start_r = -1
        start_c = -1
        for r in range(row_len):
            for c in range(col_len):
                if A[r][c] == 1:
                    start_r = r
                    start_c = c
                    break
            
        queue = deque()
        helper(A, start_r, start_c, queue)
        step = 0
        while queue:
            size = len(queue)
            for i in range(size):
                r, c = queue.popleft()
                for i, j in neighbour(r, c):
                    if A[i][j] == 1:
                        return step
                    if A[i][j] == 0:
                        A[i][j] = 2
                        queue.append((i, j))
            step += 1

