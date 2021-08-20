class Solution:

    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ls = [c for c in s]
        for i in range(0, len(s), 2 * k):
            start = i
            end = min(i + k, len(s)) - 1
            if end >= len(s):
                break
            while end > start:
                swp = ls[start]
                ls[start] = ls[end]
                ls[end] = swp
                start += 1
                end -= 1
        return ''.join(ls)
