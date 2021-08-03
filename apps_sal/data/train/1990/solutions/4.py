class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs = sorted([tuple(x) for x in pairs], key=lambda i: i[1])
        current, count = -0x3f3f3f3f, 0
        for a, b in pairs:
            if a > current:
                current = b
                count += 1
        return count
