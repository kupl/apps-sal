class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
         if s == None: return 0
         count = 0
         for item in s[-1::-1]:
             if item == ' ':
                 break
             count += 1
         return count
         '''
        count = len(s.strip().split(' ')[-1])
        return count
