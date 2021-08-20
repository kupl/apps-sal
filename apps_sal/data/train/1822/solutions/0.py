class Solution:

    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        from collections import Counter
        count = Counter(words)
        common = sorted(list(count.items()), key=lambda item: (-item[1], item[0]))[:k]
        return [w for (w, n) in common]
