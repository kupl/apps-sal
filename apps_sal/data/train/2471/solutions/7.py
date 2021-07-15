class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        robbed = [nums[0]]
        maxMoney = robbed[0]
        #print(nums)
        for i in range(1, len(nums)):
            cur = nums[i]
            for j in range(len(robbed) - 1):
                cur = max(nums[i] + robbed[j], cur)
            robbed.append(cur)
            if cur > maxMoney:
                maxMoney = cur
        #print(robbed)
        return maxMoney
        

