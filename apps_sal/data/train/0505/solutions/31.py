class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        if not s:
            return s
        stack = list()
        remove = list()
        for (idx, char) in enumerate(s):
            if char == '(':
                stack.append(idx)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    remove.append(idx)
        remove += stack
        return ''.join([char for (idx, char) in enumerate(s) if idx not in remove])
