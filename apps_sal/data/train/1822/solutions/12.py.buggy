import heapq
 import functools
 @functools.total_ordering
 class Word:
     def __init__(self, str, c):
         self.s = str
         self.c = c
     def __eq__(self, other):
         return self.c == other.c and self.s == other.c
     def __le__(self, other):
         return self.c < other.c or (self.c == other.c and self.s > other.s)
     def __repr__(self):
         return self.s + str(self.c)
 class Solution:
     def topKFrequent(self, words, k):
         """
         :type words: List[str]
         :type k: int
         :rtype: List[str]
         """
         h = []
         d = {}
         for w in words:
             c = d.get(w, 0)
             c += 1
             d[w] = c
         for w in d.keys():
             heapq.heappush(h, Word(w, d[w]))
             if len(h) > k:
                 heapq.heappop(h)
         res = []
         while len(h) > 0:
             res.append(heapq.heappop(h))
         #print(res)
         return [w.s for w in reversed(res)]
