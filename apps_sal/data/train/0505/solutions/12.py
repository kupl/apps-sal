class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        updated_s = []
        for ch in s:
            if ch not in {'(', ')'}:
                updated_s.append(ch)
            elif ch == '(':
                stack.append(len(updated_s))
                updated_s.append(ch)
            elif stack:
                updated_s.append(ch)
                stack = stack[:-1]
        if stack:
            for i in stack[::-1]:
                updated_s = updated_s[:i] + updated_s[i + 1:]
        return ''.join(updated_s)
