class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        n = len(arr)
        for i in range(1, n): # for each row after the first
            for j in range(n): # for each col
                # collect the non-adjacent cols in the prev row
                prevNonAdj = [arr[i-1][k] for k in range(n) if k != j]
                # add the min of the prev non-adj cols to the curr col
                # since modifying arr directly, sum accumulates
                arr[i][j] += min(prevNonAdj)
        return min(arr[n-1])
