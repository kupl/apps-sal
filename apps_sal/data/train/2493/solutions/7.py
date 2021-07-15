class Solution:
     def maximumProduct(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         max_num = -1000
         s_max = -1000
         t_max = -1000
         min_num = 1000
         s_min = 1000
         
         for i in range(len(nums)):
             if nums[i] > max_num:
                 t_max = s_max
                 s_max = max_num
                 max_num = nums[i]
             elif nums[i] > s_max:
                 t_max = s_max
                 s_max = nums[i]
             elif nums[i] > t_max:
                 t_max = nums[i]
             if nums[i] < min_num:
                 s_min = min_num
                 min_num = nums[i]
             elif nums[i] < s_min:
                 s_min = nums[i]
 
         print (max_num, s_max, t_max, min_num, s_min)
         a = max_num * s_max * t_max  
         b = min_num * s_min * max_num       
         if a > b:
             return(a)
         else:
             return(b)
