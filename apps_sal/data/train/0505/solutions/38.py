class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        OPEN = '('
        CLOSE = ')'
        stack = []
        for (i, c) in enumerate(s):
            if c == OPEN:
                stack.append(i)
            if stack and c == CLOSE and (s[stack[-1]] == OPEN):
                stack.pop()
                continue
            if c == CLOSE:
                stack.append(i)
        output = ''
        for (i, c) in enumerate(s):
            if i not in stack:
                output += c
        return output
