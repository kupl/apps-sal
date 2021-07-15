import collections
 import heapq
 import functools
 
 @functools.total_ordering
 class Element:
     def __init__(self, count, word):
         self.count = count
         self.word = word
         
     def __lt__(self, other):
         if self.count == other.count:
             return self.word > other.word
         return self.count < other.count
     
     def __eq__(self, other):
         return self.count == other.count and self.word == other.word
 
 class Solution(object):
     def topKFrequent(self, words, k):
         """
         :type words: List[str]
         :type k: int
         :rtype: List[str]
         """
         counts = collections.Counter(words)   
         
         heap = []
         for word, count in counts.items():
             heapq.heappush(heap, Element(count, word))
             if len(heap) > k:
                 heapq.heappop(heap)
         
         res = []
         for _ in range(k):
             res.append(heapq.heappop(heap).word)
         return res[::-1]
     
