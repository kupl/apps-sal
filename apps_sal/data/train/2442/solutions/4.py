class Solution:

    def sortString(self, s: str) -> str:
        s = sorted(s)
        ans = []
        while s:
            for i in sorted(set(s)):
                ans.append(s.pop(s.index(i)))
            for i in sorted(set(s), reverse=True):
                ans.append(s.pop(s.index(i)))
        return ''.join(ans)
