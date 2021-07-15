class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        
        N = len(A)
        M = len(A[0])
        
        #Get border of island
        def dfs(A, i, j, res, isnum):
            if not ( 0 <= i < N and 0 <= j < M): return
            if A[i][j] == 1:
                A[i][j] = isnum
                if i == 0 or i == N-1 or j == 0 or j == M -1:
                    res.append((i,j))
                elif (i != 0 and A[i-1][j] == 0) or (i != N-1 and A[i+1][j] == 0) or (j != 0 and A[i][j-1] == 0) or (j != M-1 and A[i][j+1] == 0):
                    res.append((i,j))
                for m,n in ((-1,0),(1,0),(0,-1),(0,1)):
                    dfs(A,i+m,j+n, res, isnum)
            
        def getislands(A):
            res = []
            isnum = 2
            for i, row in enumerate(A):
                for j, x in enumerate(row):
                    if A[i][j] == 1:
                        border = []
                        dfs(A, i, j, border, isnum)
                        res.append(border)
                        isnum += 1
                        print (\"A:\", A)
            return res
        
        islands = getislands(A)
        print (islands)
        is1, is2 = islands[0], islands[1]
        minflip = float(\"inf\")
        print (\"is1:\", is1, \"is2:\", is2)
        for island1 in is1:
            for island2 in is2:
                minflip = min(sum([abs(x-y) for x,y in zip(island1, island2)]), minflip)
        return minflip-1
        
