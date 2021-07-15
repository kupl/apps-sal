class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        # naive: always recomput block k*k for O(N*M) positions
        # better: for large k, compute once then advance j by removing leftcol and adding rightcol, etc
          # save rowsum and colsum O(N+M) mem then use to derive a given block?
            # BUT we can't derive middle k slices of row/col  unless we do k rows....
          # O(N*M)*()
        N,M = len(mat),len(mat[0])
        ans = [[0]*M for i in range(N)]
        
        def getBlockSum(i,j):
          # print(f'{i},{j}')
          rows = mat[max(0,i-K):i+K+1]  # [-1:2] -> empty!!
          # print(f'{rows}')
          block = list(zip(*rows))[max(0,j-K):j+K+1]
          # print(f'{block}')
          return sum(sum(blockrow) for blockrow in block)
        
        for i in range(N):
          for j in range(M):
            ans[i][j] = getBlockSum(i,j)
        
        return ans
        
        # rowSums,colSums = [0]*N,[0]*M
        # for i in range(N):
        #   rowSums[i] = sum(mat[i])
        # for j in range(M):
          # colSums[i] = sum(zip(*mat)[j])  #sum([mat[i][j] for i in range(N)])   # 
        

