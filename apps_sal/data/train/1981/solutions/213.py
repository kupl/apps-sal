from itertools import accumulate
from operator import mul
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        cums = [0 for i in range(len(nums)+1)]
        for start,end in requests:
            cums[start]+=1
            cums[end+1]-=1
        return sum( map(mul,sorted(accumulate(cums),reverse=True),sorted(nums,reverse=True) ))%(10**9+7)
