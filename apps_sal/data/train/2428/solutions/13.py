class Solution:
     def singleNumber(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         # 1,3,1,2,4,3,4
         _dict = {}
         for num in nums:
             try:
                 del _dict[num]
             except:
                 _dict[num] = True
         return list(_dict.keys())[0]
