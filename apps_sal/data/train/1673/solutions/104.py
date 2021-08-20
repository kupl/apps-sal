class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        if len(arr) == 0:
            return 0
        for i in range(1, len(arr)):
            for j in range(len(arr[0])):
                mini = float('inf')
                for k in range(len(arr[0])):
                    if k != j:
                        mini = min(mini, arr[i - 1][k])
                arr[i][j] += mini
        ans = float('inf')
        for i in range(len(arr[0])):
            ans = min(ans, arr[-1][i])
        return ans
