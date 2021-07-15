from functools import reduce
 class Solution:
     def smallestRange(self, nums):
         """
         :type nums: List[List[int]]
         :rtype: List[int]
         """
         k = len(nums)
         idx = [0]*k
         
         dic = collections.defaultdict(list)
         
         for i in range(k):
             dic[nums[i][0]].append(i)
         
         mi, ma = min(dic.keys()), max(dic.keys())
         
         ret = (mi, ma)
         while True:
             for i in dic[mi]:
                 idx[i] += 1
                 if idx[i]==len(nums[i]):
                     return ret
                 dic[nums[i][idx[i]]].append(i)
             dic.pop(mi)
             mi, ma = min(dic.keys()), max(dic.keys())
             if ma-mi<ret[1]-ret[0]:
                 ret = (mi, ma)
         
