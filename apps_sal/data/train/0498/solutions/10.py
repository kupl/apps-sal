class Solution:
     def rob_prev(self, nums):
         n = len(nums)
         if n == 0:
             return 0
         elif n < 3:
             return max(nums)
         mem = [0 for x in range(n+1) ]
         mem[0] = nums[0]
         mem[1] = max(nums[1], nums[0])
         for i in range(2,n):
             mem[i] = max(mem[i-2] + nums[i], mem[i-1])
         return mem[n-1]
     def rob(self, nums):
         n = len(nums)
         if n == 0:
             return 0
         elif n < 3:
             return max(nums)
         return max(self.rob_prev(nums[1:]), self.rob_prev(nums[:len(nums)-1]))
         
         """
         :type nums: List[int]
         :rtype: int
         """

