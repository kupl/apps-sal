class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        m = 100 * len(arr)
        T = [[0 for _ in range(len(arr))] for _ in range(len(arr))]
        T[0] = arr[0]
        for i in range(1, len(arr)):
            for j in range(len(arr)):
                temp = T[i - 1][j]
                T[i - 1][j] = m
                T[i][j] = arr[i][j] + min(T[i - 1])
                T[i - 1][j] = temp
        return min(T[-1])
