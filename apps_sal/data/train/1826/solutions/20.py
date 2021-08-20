from itertools import accumulate


class Solution:

    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        A = mat.copy()
        for i in range(len(A)):
            A[i] = [0] + list(accumulate(A[i]))
        Ans = [[0 for i in range(len(A[0]))] for j in range(len(A))]
        for i in range(len(A)):
            for j in range(1, len(A[0])):
                for p in range(max(0, i - K), min(len(A) - 1, i + K) + 1):
                    Ans[i][j] += A[p][min(j + K, len(A[0]) - 1)] - A[p][max(0, j - K - 1)]
        for i in range(len(Ans)):
            Ans[i] = Ans[i][1:]
        return Ans
