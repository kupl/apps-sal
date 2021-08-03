class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        if not arr or not arr[0]:
            raise ValueError(\"empty input.\")
        
        m = len(arr) # row
        n = len(arr[0]) # col
        dp = list(arr[0]) # start with first row.
        
        for row in arr[1:]:
            dp_new = [0] * n
            for i in range(n):
                dp_new[i] = row[i] + min([x for i_prev, x in enumerate(dp) if i != i_prev])
            dp = dp_new
            
        return min(dp_new)
