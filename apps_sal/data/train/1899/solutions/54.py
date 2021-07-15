class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        queue = []
        def markIsland2(i, j):
            if i < 0 or i >= len(A) or j < 0 or j >= len(A): return False
            if A[i][j] == 2: return False
            if A[i][j] == 0: return True
            A[i][j] = 2
            shore = False
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                shore |= markIsland2(i+x, j+y)
            if shore: queue.append((i,j))
            return False
        
        flag = False
        for i in range(len(A)):
            if flag: break
            for j in range(len(A)):
                if A[i][j] == 1:
                    markIsland2(i, j)
                    flag = True
                    break

        def BFS(i,j):
            # A[i][j] = 2
            queue.append((i,j))
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= (i+x) < len(A) and  0 <= (j+y) < len(A):
                    if A[i+x][j+y] == 1: return True
                    elif A[i+x][j+y] == 0: 
                        A[i+x][j+y] = 2
                        queue.append((i+x,j+y))
            else: return False
                  
        cnt = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                i, j = queue.pop(0)
                if BFS(i, j): return cnt
            cnt += 1
