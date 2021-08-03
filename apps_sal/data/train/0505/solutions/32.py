class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        to_remove = []
        stack = []
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            if char == ')':
                if not stack:
                    to_remove.append(i)
                else:
                    stack.pop()
        if stack:
            to_remove.extend(stack)

        output = [char for i, char in enumerate(s) if i not in to_remove]
        return ''.join(output)
