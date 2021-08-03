class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        cumMat = [[0 for _ in range(len(mat[0]) + 2)] for _ in range(len(mat) + 2)]
        cumMat[1][1] = mat[0][0]
        for i in range(2, len(mat) + 1):
            cumMat[i][1] = mat[i - 1][0] + cumMat[i - 1][1]
        for j in range(2, len(mat[0]) + 1):
            cumMat[1][j] = mat[0][j - 1] + cumMat[1][j - 1]
        for i in range(2, len(mat) + 1):
            for j in range(2, len(mat[0]) + 1):
                cumMat[i][j] = mat[i - 1][j - 1] + cumMat[i - 1][j] + cumMat[i][j - 1] - cumMat[i - 1][j - 1]

        answer = [[0 for _ in mat[0]] for _ in mat]
        for i in range(1, len(cumMat) - 1):
            for j in range(1, len(cumMat[0]) - 1):
                i1 = max(1, i - K)
                i2 = min(len(cumMat) - 2, i + K)
                j1 = max(1, j - K)
                j2 = min(len(cumMat[0]) - 2, j + K)
                # print(i1)
                # print(j1)
                # print(i2)
                # print(j2)
                answer[i - 1][j - 1] = cumMat[i2][j2] - cumMat[i1 - 1][j2] - cumMat[i2][j1 - 1] + cumMat[i1 - 1][j1 - 1]
                print(answer[i - 1][j - 1])
        return answer
