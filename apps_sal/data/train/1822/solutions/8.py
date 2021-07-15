class Solution:
     def topKFrequent(self, words, k):
         """
         :type words: List[str]
         :type k: int
         :rtype: List[str]
         """
         counter = collections.Counter(words)
         keys = list(counter.keys())
         # Notice how this answer used a tuple in sorting so that it sorts based
         # on counter value first and then string alphabetical value the second
         keys.sort(key=lambda x: (-counter[x], x))
         return keys[:k]
         

