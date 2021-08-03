class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        n = len(arr)
        for i in range(1, n):
            for j in range(len(arr[0])):
                curMin = float('inf')
                for k in range(len(arr[0])):
                    if j == k:
                        continue
                    curMin = min(curMin, arr[i - 1][k])
                arr[i][j] += curMin
            # arr[i][1] += min(arr[i - 1][0], arr[i - 1][2])
            # arr[i][2] += min(arr[i - 1][0], arr[i - 1][1])

        return min(arr[n - 1])
