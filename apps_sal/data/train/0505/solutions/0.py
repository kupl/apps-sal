class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        if not s:
            return s
        l = 0
        r = 0
        res = ''
        for (i, c) in enumerate(s):
            if c == '(':
                l += 1
            if c == ')':
                if l == r:
                    continue
                else:
                    r += 1
            res += c
        s = res
        l = 0
        r = 0
        res = ''
        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            if c == ')':
                r += 1
            if c == '(':
                if l == r:
                    continue
                else:
                    l += 1
            res = c + res
        return res
