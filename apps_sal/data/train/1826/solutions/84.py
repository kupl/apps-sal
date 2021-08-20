from itertools import accumulate as acc


class Solution:

    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        N = len(mat)
        M = len(mat[0])
        prefix = [*list(zip(*list(map(acc, list(zip(*list(map(acc, mat))))))))]
        for i in prefix:
            print(i)
        dp = [[0 for _ in range(M)] for _ in range(N)]
        for i in range(N):
            for j in range(M):
                r = min(i + K, N - 1)
                b = min(j + K, M - 1)
                l = max(0, i - K)
                t = max(0, j - K)
                cursum = prefix[r][b]
                if l - 1 >= 0:
                    cursum -= prefix[l - 1][b]
                if t - 1 >= 0:
                    cursum -= prefix[r][t - 1]
                if l - 1 >= 0 and t - 1 >= 0:
                    cursum += prefix[l - 1][t - 1]
                dp[i][j] = cursum
        return dp
