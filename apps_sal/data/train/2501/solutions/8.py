class Solution:

    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        r = []
        k_str = ''
        for i in range(len(s)):
            if i % k == 0:
                if i != 0:
                    r.append(k_str)
                k_str = s[i]
            else:
                k_str += s[i]
        r.append(k_str)
        for i in range(len(r)):
            if i % 2 == 0:
                r[i] = r[i][::-1]
        return ''.join(r)
