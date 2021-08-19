class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        rows = len(arr)
        columns = len(arr[0])
        for i in range(1, rows):
            for j in range(columns):
                minimum = float('inf')
                for k in range(columns):
                    if k != j:
                        minimum = min(minimum, arr[i - 1][k])
                arr[i][j] = arr[i][j] + minimum
        return min(arr[-1])
