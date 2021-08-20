class Solution:

    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        c = collections.Counter(words).most_common()
        res = []
        while len(res) < k:
            temp = []
            node = c.pop(0)
            temp.append(node[0])
            while c and c[0][1] == node[1]:
                node = c.pop(0)
                temp.append(node[0])
            res.extend(sorted(temp))
        return res[:k]
