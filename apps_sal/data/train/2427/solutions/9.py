class Solution:

    def findMaxConsecutiveOnes(self, nums):
        max_final = 0
        max_here = 0
        for num in nums:
            if num == 1:
                max_here += 1
                max_final = max(max_final, max_here)
            else:
                max_here = 0
        return max_final
