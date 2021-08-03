class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove = []

        for i in range(len(s)):
            if s[i] not in '()':
                continue
            elif s[i] == '(':
                stack.append(i)
            else:
                if s[i] == ')' and not stack:
                    remove.append(i)
                else:
                    stack.pop()
        stack.extend(remove)

        output = []
        for i, v in enumerate(s):
            if i not in stack:
                output.append(v)
        return ''.join(output)
