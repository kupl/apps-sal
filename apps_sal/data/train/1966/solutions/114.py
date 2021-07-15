class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        ans = 0
        N = len(mat)
        M = len(mat[0])
        row = 0 
        col = 0
        for row in range(N):
            for col in range(M):
                if mat[row][col] == 0:
                    continue
                else:
                    i = row
                    j = col
                    n = N 
                    while j < M:
                        if mat[i][j] == 0 or i == n:
                            n = i
                            i = row
                            j += 1
                        elif i+1 == N:
                            i = row
                            j += 1
                            ans += 1
                        else:
                            ans += 1
                            i += 1
        return ans

