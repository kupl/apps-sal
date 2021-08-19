class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        (stack, index, res) = ([], [], '')
        for i in range(len(s)):
            if s[i] == '(':
                stack.append((i, s[i]))
            elif s[i] == ')':
                if not stack:
                    index.append(i)
                elif stack[-1][1] == '(':
                    stack.pop()
        while stack:
            index.append(stack.pop()[0])
        for i in range(len(s)):
            if i not in index:
                res += s[i]
        return res
