class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        if not arr:
            return 0
        length = len(arr)
        for i in range(1, length):
            for j in range(length):
                if j == 0:
                    arr[i][j] += min(arr[i - 1][j + 1:])
                elif j == len(arr) - 1:
                    arr[i][j] += min(arr[i - 1][:-1])
                else:
                    arr[i][j] += min(arr[i - 1][:j] + arr[i - 1][j + 1:])
        return min(arr[-1])
