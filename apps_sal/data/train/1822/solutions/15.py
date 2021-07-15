import collections
 import heapq
 
 
 def lexical_reverse(w):
     padding = [999] * (20 - len(w))
     return (w[0], [200 - ord(x) for x in w[1]] + padding)
 
 
 class Solution:
     def topKFrequent(self, words, k):
         """
         :type words: List[str]
         :type k: int
         :rtype: List[str]
         """
         freq = collections.defaultdict(int)
         for w in words:
             freq[w] += 1
         word_pairs = []
         for w in freq.keys():
             word_pairs.append((freq[w], w))
 
         heapq.heapify(word_pairs)
         return [w[1] for w in heapq.nlargest(
             k, word_pairs, lexical_reverse)]

