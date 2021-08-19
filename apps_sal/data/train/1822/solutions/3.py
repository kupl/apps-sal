class Solution:

    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        cnt = collections.Counter(words)
        word_freq = list(cnt.items())
        word_freq.sort(key=lambda item: (-item[1], item[0]))
        return [k for (k, v) in word_freq[:k]]
