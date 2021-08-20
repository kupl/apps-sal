class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        count = 0
        ans = ''
        for idx in range(len(s)):
            if s[idx] == '(':
                count += 1
                ans += s[idx]
            elif s[idx] == ')':
                if count > 0:
                    count -= 1
                    ans += s[idx]
            else:
                ans += s[idx]
        idx = len(ans) - 1
        while count > 0:
            if ans[idx] == '(':
                ans = ans[:idx] + ans[idx + 1:]
                count -= 1
            idx -= 1
        return ans
