class Solution:
     def topKFrequent(self, words, k):
         """
         :type words: List[str]
         :type k: int
         :rtype: List[str]
         """
         from collections import Counter
         c = Counter(words)
         buckets = [[] for _ in range(len(words)+1)]
         for key in c:
             buckets[c[key]].append(key)
         for b in buckets:
             b.sort()
         ans = []
         i = len(buckets) - 1
         while i >= 0:
             if len(ans) + len(buckets[i]) < k:
                 ans += buckets[i]
             else:
                 ans += buckets[i][:k - len(ans)]
                 break
             i -= 1
         return ans
 
 
 def __starting_point():
     s = Solution()
     print(s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
__starting_point()
