class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        n = len(arr)
        m = len(arr[0])
        for i in range(1,n):
            for j in range(m):
                arr[i][j] += min(arr[i-1][0:j]+arr[i-1][j+1:])
        return min(arr[-1])
