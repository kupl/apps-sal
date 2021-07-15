class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        max_to_i = [None] * n
        max_to_i[0] = nums[0]
        max_to_i[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            max_to_i[i] = max(nums[i] + max_to_i[i-2], max_to_i[i-1])
            
        # max_to_i has len n, and contains max with the subarray [0:i].
        # Total result is just max_to_i[n-1]
        
        return max_to_i[-1]
