class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        to_remove = set()
        stack = []

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if len(stack):
                    stack.pop()
                    continue
                to_remove.add(i)

        for i in stack:
            to_remove.add(i)

        st = ''
        for i, c in enumerate(s):
            if i not in to_remove:
                st += c

        return ''.join(st)
