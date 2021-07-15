class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        total = 0
        for row in range(len(arr)-1):
            row1_min, row2_min = min(arr[row]), min(arr[row+1])
            i1, i2 = arr[row].index(row1_min), arr[row+1].index(row2_min)
            if i1 != i2:
                total += row1_min
            else:
                total = False
                break
        if total:
            return total + min(arr[-1])
        dp = [[arr[j][i] if j == 0 else float('inf') for i in range(len(arr))] for j in range(len(arr))]
        for row in range(len(arr)-1):
            for col in range(len(arr[row])):
                for next_col in range(len(arr[row])):
                    if next_col != col:
                        dp[row+1][next_col] = min(dp[row+1][next_col], dp[row][col] + arr[row+1][next_col])
        return min(dp[len(arr)-1])
