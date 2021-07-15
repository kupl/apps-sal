from itertools import combinations
import numpy
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        res = (nums[-1]-1)*(nums[-2]-1)
        return res

