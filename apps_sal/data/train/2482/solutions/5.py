class Solution:
     def canPlaceFlowers(self, nums, n):
         """
         :type flowerbed: List[int]
         :type n: int
         :rtype: bool
         """
         count = 0
         nums = [0] + nums +[0]
         for i in range(1,len(nums)-1):
             if nums[i] == 0:
                 if nums[i+1] == 0 and nums[i-1] == 0:
                     count += 1
                     nums[i] =1
         if count >= n:
             return True
         else:
             return False
