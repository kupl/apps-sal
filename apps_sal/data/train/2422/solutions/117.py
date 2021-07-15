from itertools import combinations

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        arr = combinations(nums, 2)
        res = []
        
        for x in arr:
            res.append((x[0] - 1) * (x[1] - 1))
        
        return max(res)
