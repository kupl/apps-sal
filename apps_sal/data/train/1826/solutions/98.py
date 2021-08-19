class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        if not mat or not mat[0]:
            return mat
        answer = [[0 for _ in mat[0]] for _ in mat]
        # create left->right horizontal running sums in each row of mat
        for i in range(len(mat)):
            for j in range(1, len(mat[0])):
                mat[i][j] += mat[i][j - 1]
        # create horizontal 2K+1-sums in answer
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                answer[i][j] = mat[i][min(j + K, len(mat[i]) - 1)]
                if j - K > 0:
                    answer[i][j] -= mat[i][j - K - 1]
        mat, answer = answer, [[0 for _ in mat[0]] for _ in mat]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                answer[i][j] = sum([mat[k][j] for k in range(max(0, i - K), min(len(mat), i + K + 1))])

        return answer
