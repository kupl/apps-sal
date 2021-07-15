class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        for i in range(1, n:=len(arr)):
            for j in range(n):
                t = min(arr[i-1][0:j] + arr[i-1][j+1:n])
                arr[i][j] += t
                
        return min(arr[-1])
