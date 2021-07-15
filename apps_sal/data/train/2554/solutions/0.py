class Solution:
     def longestWord(self, words):
         """
         :type words: List[str]
         :rtype: str
         """
         
         result = "";
         wordSet = set(words);
         for word in words:
             if (len(word) > len(result) or len(word) == len(result) and word < result) and all(word[ : i] in wordSet for i in range(1, len(word))):
                 result = word;
                 
         return result;
