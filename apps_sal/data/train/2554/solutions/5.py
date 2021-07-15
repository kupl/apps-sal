class Solution:
     def longestWord(self, words):
         """
         :type words: List[str]
         :rtype: str
         """
         valid = {''}
         for word in sorted(words):
             if word[:-1] in valid:
                 valid.add(word)
         return max(sorted(valid), key = len)
