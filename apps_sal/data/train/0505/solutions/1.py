class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        to_remove = set()
        for (i, c) in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    to_remove.add(i)
        print(to_remove)
        to_remove |= set(stack)
        print(to_remove)
        return ''.join((c for (i, c) in enumerate(s) if i not in to_remove))
