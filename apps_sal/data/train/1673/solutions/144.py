class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        n= len(arr)
        for i in range(1, n):
            r= heapq.nsmallest(2, arr[i-1])
            for j in range(n):
                arr[i][j]+= r[1] if arr[i-1][j]== r[0] else r[0]
                
        return min(arr[-1])
