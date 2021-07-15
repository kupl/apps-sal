import numpy as np

class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        dp = arr[0]
        
        
        for r in range(1, len(arr)):
            new_dp = [i for i in dp]
            for c in range(len(arr)):
                lst = [dp[j] for j in range(len(arr)) if j != c]
                
                new_dp[c] = min(lst)+arr[r][c]
            dp = new_dp
        return int(min(dp))

