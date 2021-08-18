class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        num = 1
        i = 0
        sum = num
        while i < len(nums):
            sum += nums[i]
            if sum < 1:
                flag = False
                i = 0
                num += 1
                sum = num

            else:
                i += 1
        return num
