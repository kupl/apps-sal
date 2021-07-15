class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        for i in range(m):
            for j in reversed(range(n-1)):
                if mat[i][j] == 1:
                    mat[i][j] = mat[i][j+1] + 1               

        def countSubmat(i, j):
            top = i
            left = j
            bound = n
            counter = 0
            while i < m and mat[i][j] > 0:
                counter += min(bound, mat[i][j])
                bound = min(bound, mat[i][j])
                i += 1
            return counter
        
        total = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] > 0:
                    total += countSubmat(i, j)
        
        return total
