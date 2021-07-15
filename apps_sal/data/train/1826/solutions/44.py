class Solution:
    def matrixBlockSum(self, mat, K):


        def idx(i, j):

            return i * len(mat[j]) + j

        prefixSum = dict()
        prefixSum[-1] = 0
        currSum = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                currSum += mat[i][j]
                prefixSum[idx(i, j)] = currSum

        answer = [[0 for c in range(len(mat[r]))] for r in range(len(mat))]

        for r in range(len(mat)):
            for c in range(len(mat[r])):
                currSum = 0
                for i in range(max(r - K, 0), min(r + K + 1, len(mat))):
                    currSum += prefixSum[idx(i, min(c + K, len(mat[i]) - 1))] - \\
                        prefixSum[idx(i, max(c - K, 0) - 1)]

                answer[r][c] = currSum

        return answer

        
        
