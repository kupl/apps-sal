class Solution:
    def maxProduct(self, nums):
        result = 0
        altnums = []
        for num in nums:
            altnums.append(num)
        for i in range(len(nums)):
            if nums[i] == max(nums):
                altnums[i] = 0
                break
        print(altnums, nums)
        result = (max(nums)-1) * (max(altnums)-1)
        return result
