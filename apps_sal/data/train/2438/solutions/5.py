class Solution:
     def lengthOfLastWord(self, s):
         """
         :type s: str
         :rtype: int
         """
         spaces = 0
         word_started = False
         # Traverse through string from back
         # Count number of spaces encountered before first word starts
         # Keep going through characters until next space is found
         # Return that index (minus one, not counting the space)
         # And subtract the number of spaces
         for i in range(1, len(s) + 1):
             if s[-i] == " " and word_started is False:
                 spaces += 1
             elif s[-i] == " " and word_started is True:
                 return i - 1 - spaces
             else:
                 word_started = True
         if word_started is True:
             return len(s) - spaces
         else:
             return 0
