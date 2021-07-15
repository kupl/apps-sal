class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        row_size,col_size = len(mat),len(mat[0])
        ans = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        for x in mat:
            for _ in range(K):
                x.append(0)
                x.insert(0,0)
        row = [[0 for _ in range(len(mat[0]))] for _ in range(K)]
        mat =  row + mat + row
        print(mat)
        
        for r in range(K,K+row_size):
            for c in range(K,K+col_size):
                ans[r-K][c-K] = sum(sum(s[c-K:c+K+1]) for s in mat[r-K:r+K+1])
        return ans

