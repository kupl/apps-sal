class Solution:

    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counter = collections.Counter(words)
        keys = list(counter.keys())
        keys.sort(key=lambda x: (-counter[x], x))
        return keys[:k]
