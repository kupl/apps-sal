import functools
 import collections
 
 class Solution(object):
     def topKFrequent(self, words, k):
         """
         :type words: List[str]
         :type k: int
         :rtype: List[str]
         """
         wordCounts = collections.Counter(words)
         candidates = list(wordCounts.keys())
         candidates.sort(key = lambda word: (-wordCounts[word], word))
         return candidates[:k]
           
