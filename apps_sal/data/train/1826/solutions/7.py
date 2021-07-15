class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        
        rows = collections.defaultdict(list)
        
        for i,row in enumerate(mat):
            s = 0
            for v in row:
                s+=v
                rows[i].append(s)
        # print(rows)
            
        m,n = len(mat), len(mat[0])
        ans = [ [0]*n for _ in range(m) ]
        for i in range(m):
            for j in range(n):
                ind = [max(0,j-K), min(n-1,j+K)]
                
                # print((i,j),(max(0,i-K), min(m,i+K+1)),ind)
                for k in range(max(0,i-K), min(m,i+K+1)):
                    sum = rows[k][ind[1]]
                    if ind[0]>0: sum = rows[k][ind[1]]- rows[k][ind[0]-1]
                    
                    # print((k,ind),sum)
                    ans[i][j]+=sum
                # print('--------------------')
        return ans
