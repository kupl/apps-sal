class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n = len(nums)
        
        startValue = 1
        
        while startValue < float('inf'):
            get = True
            tmp = startValue
            for i in range(n):
                if nums[i] + tmp < 1:
                    get = False
                    break
                tmp = nums[i] + tmp
            if not get: 
                startValue += 1
            else:
                return startValue
