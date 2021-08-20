class Solution:

    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs = sorted(pairs, key=lambda t: t[0])
        (p, L) = (None, 0)
        for t in sorted(pairs, key=lambda t: t[1]):
            if p is None or t[0] > p:
                (p, L) = (t[1], L + 1)
        return L
