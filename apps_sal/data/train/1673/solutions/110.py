class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        if arr is None or len(arr) == 0 or len(arr[0]) == 0:
            return 0
        for i in range(1, len(arr)):
            for j in range(len(arr[0])):
                temp = float('inf')
                for last_col in range(len(arr[0])):
                    if last_col != j:
                        temp = min(temp, arr[i - 1][last_col])
                arr[i][j] += temp
        ans = float('inf')
        for i in range(len(arr[0])):
            ans = min(ans, arr[-1][i])
        return ans
