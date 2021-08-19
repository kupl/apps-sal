class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        for row in range(1, len(arr)):
            for col in range(0, len(arr)):
                if col == 0:
                    arr[row][col] += min(arr[row - 1][1:])
                elif col == len(arr) - 1:
                    arr[row][col] += min(arr[row - 1][:-1])
                else:
                    arr[row][col] += min(arr[row - 1][:col] + arr[row - 1][col + 1:])
        return min(arr[-1])
