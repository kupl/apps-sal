class Solution:
     def singleNumber(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         mydict = {}
         for i in nums:
             if i not in mydict.keys():
                 mydict[i] = 1
             else:
                 if mydict[i] >= 2:
                     return i
                 mydict[i] = mydict[i] + 1
         for key, value in mydict.items():
             if value != 2:
                 return key
