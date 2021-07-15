import random
 
 class Solution:
 
     def __init__(self, nums):
         """
         :type nums: List[int]
         """
         
         self.nums = nums
         
 
     def pick(self, target):
         """
         :type target: int
         :rtype: int
         """
         
         result = None
         seen = 0
         
         for i, num in enumerate(self.nums):
             
             if num == target:
                 
                 if not result:
                     result = i
                 else:
                     #
                     if random.randint(0, seen) == 0:
                         result = i
                 
                 seen += 1
         
         print("saw", seen)
         
         return result
 
 
 # Your Solution object will be instantiated and called as such:
 # obj = Solution(nums)
 # param_1 = obj.pick(target)
