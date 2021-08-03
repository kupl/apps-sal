class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ans = ''
        stack = []
        to_delete_idx = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append('(')
                to_delete_idx.append(i)
            if s[i] == ')':
                if not stack or stack[-1] == ')':
                    stack.append(')')
                    to_delete_idx.append(i)
                else:
                    stack.pop()
                    to_delete_idx.pop()
        for i in range(len(s)):
            if i not in to_delete_idx:
                ans += s[i]

        return ans
