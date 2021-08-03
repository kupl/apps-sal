class Solution:
    def longestPalindrome(self, s):

        l = list(s)
        result = 0

        for x in set(s):
            x_count = l.count(x)
            if x_count % 2 == 0:
                result += x_count
            else:
                result += x_count - 1

        if len(l) > result:
            result += 1

        return result
