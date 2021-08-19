class Solution:

    def modifyString(self, s: str) -> str:
        letters = ['a', 'b', 'c']
        for i in range(len(s)):
            if s[i] == '?':
                for l in letters:
                    if (i == 0 or s[i - 1] != l) and (i == len(s) - 1 or s[i + 1] != l):
                        s = s.replace('?', l, 1)
                        break
        return s
