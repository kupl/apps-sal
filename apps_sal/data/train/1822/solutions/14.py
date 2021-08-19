class Solution:

    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        wDict = collections.Counter(words)
        res = []
        maxHeap = []
        for (key, cnt) in list(wDict.items()):
            heapq.heappush(maxHeap, (-cnt, key))
        for i in range(k):
            (freq, word) = heapq.heappop(maxHeap)
            res.append(word)
        return res
