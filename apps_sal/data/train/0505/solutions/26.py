class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        skip = []
        for i, c in enumerate(s):
            if c in '()':
                if c == '(':
                    stack.append(i)
                else:
                    if stack:
                        stack.pop()
                    else:
                        skip.append(i)

        while stack:
            skip.append(stack.pop())

        t = []
        for i, c in enumerate(s):
            if i not in skip:
                t.append(c)
        return ''.join(t)
