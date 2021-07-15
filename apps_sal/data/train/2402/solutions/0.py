class Solution:
     def reverseWords(self, s):
         """
         :type s: str
         :rtype: str
         """
         rev_str = s[::-1]
         rev_arr = rev_str.split()
         final = rev_arr[::-1]
         
         return ' '.join(map(str, final))
 

