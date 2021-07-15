class Solution:
     def firstUniqChar(self, s):
         """
         :type s: str
         :rtype: int
         """
         """
         dict1 = {}
         dict2 = {}
         lst = []
         
         for i in range(len(s)):
             dict1[s[i]] = dict1.get(s[i],0) + 1
             if s[i] not in dict2.keys():
                 dict2[s[i]] = i
         
         for key in dict1.keys():
             if dict1[key] == 1:
                 lst.append(dict2[key])
         
         lst.sort()
         if len(lst) > 0:
             return lst[0]
         return -1
         """
         # Don't get count for each word in s. Get the freq for each letters in 26 lower case char instead.
         letters = 'abcdefghijklmnopqrstuvwxyz'
         lst = [s.index(l) for l in letters if s.count(l) == 1]
         if len(lst) > 0:
             return min(lst)
         else:
             return -1
