class Solution:
     def singleNumber(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
 
         single_one={nums[0]}
         for i in nums[1:]:
             if i in single_one:
                 single_one.remove(i)
                 continue
             else:
                 single_one.add(i)
             if single_one=={}:
                 single_one.add(i)
         return single_one.pop()

