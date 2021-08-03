import heapq
 import functools
 
 
 @functools.total_ordering
 class Element:
     def __init__(self, word, count):
         self.word = word
         self.count = count
     
     def __eq__(self, other):
         return self.count == other.count and self.word == other.word
 
     def __gt__(self, other):
         if self.count == other.count:
             return self.word < other.word
         return self.count > other.count
 
 
 class Solution:
     def topKFrequent(self, words, k):
         """
         :type words: List[str]
         :type k: int
         :rtype: List[str]
         """
         heap = []
         for word, count in collections.Counter(words).items():
             heapq.heappush(heap, Element(word, count))
             if len(heap) > k:
                 heapq.heappop(heap)
         return [i.word for i in sorted(heap, reverse=True)]

