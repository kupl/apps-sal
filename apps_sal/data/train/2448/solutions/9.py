class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count_map, has_odd, ans = {}, 0, 0

        for c in s:
            try:
                count_map[c] += 1
            except KeyError:
                count_map[c] = 1

        for count in list(count_map.values()):
            if ans % 2 != 0 and count % 2 != 0:
                ans += count - 1
            else:
                ans += count

        return ans
