class Solution:
     def firstUniqChar(self, s):
         """
         :type s: str
         :rtype: int
         """
         buffer = {}
         repeated = set()
         for i in range(len(s)):
             char = s[i]
             if char in repeated:
                 continue
                 
             if char in buffer:
                 del(buffer[char])
                 repeated.add(char)
             else:
                 buffer[char] = i
         if not buffer:
             return -1
         
         return sorted(list(buffer.items()), key=lambda x:x[1])[0][1]

