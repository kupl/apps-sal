class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        answer = [[0] * m for i in range(n)]
        r = 0
        c = 0
        
        for i in range(n):
            tmp = []
            for j in range(m):
                if i - K < 0:
                    r = 0
                else:
                    r = i-K
                
                sum1 = 0
                while r <= i+K and r < n:
                    if j-K < 0:
                        if j+K < m:
                            sum1 += sum(mat[r][:j+K+1])
                        else:
                            sum1 += sum(mat[r])
                    else:
                        if j+K < m:
                            sum1 += sum(mat[r][j-K:j+K+1])
                        else:
                            sum1 += sum(mat[r][j-K:])
                        
                    r += 1
                answer[i][j] = sum1
            
        return answer
