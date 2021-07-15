from collections import Counter
 class Solution:
     def reorganizeString(self, S):
         """
         :type S: str
         :rtype: str
         """
         count = Counter(S)
         mylist = count.most_common()
         _, maxfreq = mylist[0]
 
         if maxfreq > (len(S) + 1) // 2:
             return ""
         else:
             res = [[] for _ in range(maxfreq)]
             start = 0
             for char, freq in mylist:
                 for i in range(freq):
                     res[(i + start) % maxfreq].append(char)
                 start += freq
             return "".join("".join(temp) for temp in res)
