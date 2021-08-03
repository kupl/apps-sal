class Solution:
    def rob(self, nums: List[int]) -> int:
        prevMax = 0
        currMax = 0

        for num in nums:
            temp = currMax
            currMax = max(prevMax + num, currMax)
            prevMax = temp

        return currMax
