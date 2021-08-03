class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        largeNumber = 0
        secondNumber = 0

        for i in nums:
            if i > largeNumber:
                largeNumber = i
        for j in nums:
            if j > secondNumber and j != largeNumber:
                secondNumber = j

        for x in range(0, len(nums)):
            for y in range(x + 1, len(nums)):
                if nums[x] == nums[y] and nums[x] == largeNumber:
                    secondNumber = largeNumber

        return int((largeNumber - 1) * (secondNumber - 1))
