class Solution:
     def singleNumber(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         dic = dict()
         for num in nums:
             if num not in list(dic.keys()):
                 dic[num]=1
             else:
                 dic[num]+=1
         for key, val in list(dic.items()):
             if val == 1:
                 return key
         
         
         

