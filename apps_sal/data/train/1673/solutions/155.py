class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:

        m = len(arr)

        for i in range(1, m):
            min1 = min(arr[i - 1])
            ind = arr[i - 1].index(min1)
            for j in range(m):
                if ind == j:
                    arr[i][j] = arr[i][j] + min(arr[i - 1][0:j] + arr[i - 1][j + 1:])
                else:
                    arr[i][j] = arr[i][j] + min1
        return min(arr[-1])
