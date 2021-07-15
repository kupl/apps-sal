class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        req = 0
        for i in range(1,len(nums)):
            for j in range(i):
                req = max(req, (nums[i]-1)*(nums[j]-1))
        return req

