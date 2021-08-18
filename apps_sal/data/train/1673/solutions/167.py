class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:

        for i in range(1, len(arr)):
            for j in range(len(arr[0])):

                arr[i][j] += min(arr[i - 1][:j] + arr[i - 1][j + 1:])

        return min(arr[-1])
