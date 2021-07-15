class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mp = float('-inf')
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                mp = max(mp, (nums[i]-1)*(nums[j]-1))
        return mp
