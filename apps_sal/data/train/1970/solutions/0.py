class Solution:

    def nearestPalindromic(self, num):
        """
        :type n: str
        :rtype: str
        """
        K = len(num)
        candidates = set([10 ** K + 1, 10 ** (K - 1) - 1])
        Prefix = int(num[:(K + 1) // 2])
        for start in map(str, [Prefix - 1, Prefix, Prefix + 1]):
            candidates.add(start + [start, start[:-1]][K & 1][::-1])
        candidates.discard(num)
        return str(min(candidates, key=lambda x: (abs(int(x) - int(num)), int(x))))
