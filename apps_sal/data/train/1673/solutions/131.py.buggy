\"\"\"
dp[r][c] = min(dp[r-1][c1], dp[r-1][c2]) for any c1, c2 != c

Base case:

dp[r][c] = 0 for r < 0

Complexity:

Time = r * c
\"\"\"

# TLE for top down

# class Solution:
#     def minFallingPathSum(self, arr: List[List[int]]) -> int:
#         rows, cols = len(arr), len(arr[0])
        
#         @lru_cache(None)
#         def dp(r, c):
#             if r < 0:
#                 return 0
            
#             return arr[r][c] + min(dp(r-1, c1) for c1 in range(cols) if c1 != c)
    
#         return min(dp(rows-1, c) for c in range(cols))

class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        rows, cols = len(arr), len(arr[0])
        prev_row = [0] * cols
    
        for r in range(rows):
            min1, min2 = heapq.nsmallest(2, prev_row)
            prev_row = [arr[r][c] + (min1 if min1 != prev_row[c] else min2) for c in range(cols)]
        
        return min(prev_row)
                        
