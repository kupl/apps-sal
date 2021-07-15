class Solution:
    def sortString(self, s: str) -> str:
        s = list(s)
        ans = ''
        while s:
            for c in sorted(set(s)):
                ans += c
                s.remove(c)
            for c in sorted(set(s), reverse = True):
                ans += c
                s.remove(c)
        return ans

