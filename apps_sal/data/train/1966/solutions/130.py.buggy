class Solution:
    def helper(self, mat, a, b):
        N = len(mat)
        M = len(mat[0])
        
        bound = M
        count = 0
        
        for r in range(a, N):
            for c in range(b, bound):                
                if mat[r][c] == 1: 
                    if (a,b) == (0,0):
                        print(\"!! rc\", r,c)
                    count += 1
                else:
                    bound = c
                    break
        return count
                
        
        
    def numSubmat(self, mat: List[List[int]]) -> int:
        N = len(mat)
        if N == 0: return 0
        M = len(mat[0])
        count = 0 
        
        for r in range(N):
            for c in range(M):
                out = self.helper(mat, r, c)
                print(\"!\", r, c, out)
                count += out
        
        return count
