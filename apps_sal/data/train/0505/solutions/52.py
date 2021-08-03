class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        to_remove = []
        stack = []

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if len(stack):
                    stack.pop()
                    continue
                to_remove.append(i)

        to_remove.extend(stack)

        s = list(s)
        for i in to_remove:
            s[i] = ''

        return ''.join(s)
