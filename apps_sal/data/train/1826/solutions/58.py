class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        answer = [[0 for i in range(n)] for i in range(m)]
        
        '''
        answer[i][j] = sum(mat[r][c]) 
            for K <= r <= i + K 
            for j - K <= c <= j + K
        '''
        
        for i in range(n):
            for j in range(m):
                c_lower = max(0, i - K)
                c_upper = min(i + K + 1, n)
                r_lower = max(0, j - K)
                r_upper = min(j + K + 1, m)
                print((m, n))
                print(((r_lower, r_upper),(c_lower, c_upper)))
                answer[j][i] = sum([mat[r][c] for r in range(r_lower, r_upper) for c in range(c_lower, c_upper)])
                
        return answer

