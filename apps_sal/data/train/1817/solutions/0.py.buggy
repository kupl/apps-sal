from collections import Counter
 
 
 class Solution:
     def reorganizeString(self, S):
         """
         :type S: str
         :rtype: str
         """
         if len(S) <= 1:
             return S
 
         chars = [char for char, count in Counter(S).most_common() for _ in range(count)]
         h = math.ceil(len(chars) / 2)
         chars[::2], chars[1::2] = chars[:h], chars[h:]
         if chars[0] == chars[1]:
             return ''
         else:
             return ''.join(chars)
         
         
