class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        for i in range(len(arr) - 2, -1, -1):
            for j in range(len(arr[0])):
                arr[i][j] += min(arr[i + 1][:j] + arr[i + 1][j + 1:])
        return min(arr[0])
