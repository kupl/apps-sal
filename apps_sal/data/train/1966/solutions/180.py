class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        count = 0
        # dp = [[0]*m for _ in range(n)]
        for i in range(n):
            c = 0
            for j in range(m-1, -1, -1):
                if mat[i][j]:
                    c += 1
                    mat[i][j] = c
                else:
                    c = 0
                
        # print(dp)
        for j in range(m):
            # print('j:',j)
            for i in range(n):
                if mat[i][j]:
                    # print('i:',i)
                    min_v = mat[i][j]
                    count += mat[i][j]
                    # print('count:', count)
                    for k in range(i+1,n):
                        # print('k:',k)
                        if not mat[k][j]: break
                        min_v = min(min_v, mat[k][j])
                        # print('min_v:',min_v)
                        count+= (k-i+1)*min_v - (k-i)*min_v
                        # print('count:', count)
                    # print()
        return count
                    
                

