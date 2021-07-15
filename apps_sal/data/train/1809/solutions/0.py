class Solution:
     def productExceptSelf(self, nums):
         """
         :type nums: List[int]
         :rtype: List[int]
         """
         nums0 = nums.copy()
         son = 1
         if 0 in nums0:
             nums0.remove(0)
             for i in nums0:
                 son *= i
             
             
         pro = 1
         for i in nums:
             pro *= i
         result = []
         for i in nums:
             if i == 0:
                 result.append(son)
             else:
                 result.append(pro//i)
         return result
