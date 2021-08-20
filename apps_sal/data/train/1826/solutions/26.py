class Solution:

    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        answer = [[0] * m for i in range(n)]
        maxo = max
        sumo = sum
        for i in range(n):
            for j in range(m):
                r = maxo(0, i - K)
                sum1 = 0
                while r <= i + K and r < n:
                    if j - K < 0:
                        if j + K < m:
                            sum1 += sumo(mat[r][:j + K + 1])
                        else:
                            sum1 += sumo(mat[r])
                    elif j + K < m:
                        sum1 += sumo(mat[r][j - K:j + K + 1])
                    else:
                        sum1 += sumo(mat[r][j - K:])
                    r += 1
                answer[i][j] = sum1
        return answer
