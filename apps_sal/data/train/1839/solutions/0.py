class Solution:
     def swimInWater(self, grid):
         """
         :type grid: List[List[int]]
         :rtype: int
         """
         N = len(grid)
         if N == 1:
             return 0
         
         eleD = {}
         for i in range(N):
             for j in range(N):
                 eleD[grid[i][j]] = (i,j)
 
 
         C = [[0 for _ in range(N)] for _ in range(N)]
         stack = set()
         nextstack = set()
         nextstack.add((0,0))
         for t in range(grid[0][0],N*N):
             if eleD[t] not in nextstack:
                 continue
             stack.add(eleD[t])
             nextstack.remove(eleD[t])
             while stack:
                 (x,y) = stack.pop()
                 if x == N-1 and y == N-1:
                     return t
                 C[x][y] = 1
                 if x > 0:
                     P = (x-1,y)
                     if C[P[0]][P[1]] == 0:
                         if grid[P[0]][P[1]] <= t:
                             stack.add(P)
                         else:
                             nextstack.add(P)
                 if y > 0:
                     P = (x,y-1)
                     if C[P[0]][P[1]] == 0:
                         if grid[P[0]][P[1]] <= t:
                             stack.add(P)
                         else:
                             nextstack.add(P)
                 if x < N-1:
                     P = (x+1,y)
                     if C[P[0]][P[1]] == 0:
                         if grid[P[0]][P[1]] <= t:
                             stack.add(P)
                         else:
                             nextstack.add(P)
                 if y < N-1:
                     P = (x,y+1)
                     if C[P[0]][P[1]] == 0:
                         if grid[P[0]][P[1]] <= t:
                             stack.add(P)
                         else:
                             nextstack.add(P)
             print(t)
                 
                 
 
         # eleD = {}
         # for i in range(N):
         #     for j in range(N):
         #         eleD[grid[i][j]] = (i,j)
         # res = grid
         # for t in range(N*N):
         #     (x,y) = eleD[t]
         #     if x > 0:
         #         if res[x-1][y] <= t:
         #             temp = res[x-1][y]
         #             for i in range(N):
         #                 for j in range(N):
         #                     if res[i][j] == temp:
         #                         res[i][j] = t
         #     if y > 0:
         #         if res[x][y - 1] <= t:
         #             temp = res[x][y - 1]
         #             for i in range(N):
         #                 for j in range(N):
         #                     if res[i][j] == temp:
         #                         res[i][j] = t
         #     if x < N - 1:
         #         if res[x + 1][y] <= t:
         #             temp = res[x + 1][y]
         #             for i in range(N):
         #                 for j in range(N):
         #                     if res[i][j] == temp:
         #                         res[i][j] = t
         #     if y < N - 1:
         #         if res[x][y + 1] <= t:
         #             temp = res[x][y + 1]
         #             for i in range(N):
         #                 for j in range(N):
         #                     if res[i][j] == temp:
         #                         res[i][j] = t
         #     #print(t,res)
         #     if res[0][0] == res[N-1][N-1]:
         #         return t

