class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                # prod = (nums[i]-1) * (nums[j]-1)
                # if prod > result:
                    # result = prod
                result = max(result, (nums[i]-1) * (nums[j]-1))
        return result

