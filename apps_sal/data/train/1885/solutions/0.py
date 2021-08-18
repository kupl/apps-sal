class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0]
        while len(ans) < num + 1:
            ans += [1 + x for x in ans]
        return ans[:num + 1]
