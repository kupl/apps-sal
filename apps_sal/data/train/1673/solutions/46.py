class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        dp_mtx = [[0] * len(arr[0]) for _ in range(len(arr))]

        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if i == 0:
                    dp_mtx[i][j] = arr[i][j]
                else:
                    dp_mtx[i][j] = arr[i][j] + min(dp_mtx[i - 1][k] for k in range(len(arr[0])) if k != j)

        return min(dp_mtx[len(arr) - 1])
