from functools import lru_cache

class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        if not arr:
            return 0
        
        cols = set(range(len(arr[0])))
        
        @lru_cache(maxsize=None)
        def path_sum(row, col):
            ret = arr[row][col]
            if row == len(arr) - 1:
                return ret
            
            other_cols = cols - {col}
            ret += min(path_sum(row+1,_) for _ in other_cols)
            return ret
        
        return min(path_sum(0, _) for _ in cols)
