class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        s = self.remove_invalid(s)
        s = self.remove_invalid(s[::-1], ')')
        return s[::-1]

    def remove_invalid(self, s, end='('):
        new_s = ''
        count = 0
        for i in range(len(s)):
            if s[i] not in ('(', ')'):
                new_s += s[i]
                continue
            count += 1 if s[i] == end else -1
            if count < 0:
                count = 0
            else:
                new_s += s[i]
        return new_s
