class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        l = []
        i = 0
        c = 0
        strlen = len(s)
        while(i < strlen):
            if(c % 2):
                l.append(s[i:i + k])
            else:
                temp = s[i:i + k]
                l.append(temp[::-1])
            c = c + 1
            i = i + k
        return ''.join(l)
