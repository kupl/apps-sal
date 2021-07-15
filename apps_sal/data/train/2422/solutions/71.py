class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]-1)*(nums[j]-1) > max_product:
                    max_product = (nums[i]-1)*(nums[j]-1)
        return max_product

