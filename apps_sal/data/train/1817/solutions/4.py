class Solution:
     def reorganizeString(self, S):
         """
         :type S: str
         :rtype: str
         """
         from math import ceil
         dict1 = {}
         s = ""
         for i in range(len(S)):
             if S[i] not in dict1:
                 dict1[S[i]] = 1
             else:
                 dict1[S[i]] += 1
             if dict1[S[i]] > ceil(len(S)/2): return ""
         dict2 = [ item for item in list(dict1.items())]
         dict2.sort(key=lambda x:x[1], reverse=True)
         for i in range(dict2[0][1]):
             s = s + dict2[0][0]
         for i in range(1,len(dict2)):
             temp = 0
             value =  dict2[i][1]
             key = dict2[i][0]
             while value>0:
                 for j in range(i):
                     while value > 0 and (dict2[j][0]+ dict2[j][0]) in s:
                         s = s[0:s.index(dict2[j][0]+ dict2[j][0])] + dict2[j][0]+ key + dict2[j][0] + s[s.index(dict2[j][0]+ dict2[j][0])+2:]
                         value -= 1
                 if value>0:
                     if key in s:
                         temp = s.index(key)
                         if temp>=2:
                             s = s[0:temp-2] + key + s[temp-2:]
                         else:
                             s = key + s
                         value -= 1
                     else:
                         s = s + key
                         value -= 1
         return s

