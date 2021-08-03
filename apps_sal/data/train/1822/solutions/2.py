class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        from collections import Counter
        return [item[0] for item in sorted(Counter(words).items(), key=lambda x: (-x[1], x[0]))[:k]]
