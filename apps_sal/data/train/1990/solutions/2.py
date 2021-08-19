class Solution:

    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key=lambda x: x[1])
        cur = pairs[0][0] - 1
        ans = 0
        for (a, b) in pairs:
            if cur < a:
                cur = b
                ans += 1
        return ans
