class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        answer = [[0] * m for i in range(n)]

        maxo = max
        sumo = sum
        mino = min
        for i in range(n):
            for j in range(m):
                r = maxo(0, i - K)
                sum1 = 0
                while r <= i + K and r < n:
                    sum1 += sumo(mat[r][maxo(0, j - K):mino(m, j + K + 1)])

                    r += 1
                answer[i][j] = sum1

        return answer
