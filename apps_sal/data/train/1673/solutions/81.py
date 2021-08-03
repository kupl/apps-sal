class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:

        m = len(arr)

        for i in range(1, m):
            for j in range(m):
                res = float('inf')
                for x in range(m):
                    if x != j:
                        if arr[i][j] + arr[i - 1][x] < res:
                            res = arr[i][j] + arr[i - 1][x]
                arr[i][j] = res

        return min(arr[-1])
