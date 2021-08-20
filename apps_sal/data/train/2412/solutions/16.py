class Solution:

    def removeDuplicates(self, s: str) -> str:
        stack = [0]
        for i in range(len(s)):
            if s[i] == stack[-1]:
                stack.pop()
                continue
            if s[i] != stack[-1]:
                stack.append(s[i])
        res = ''
        for i in range(1, len(stack)):
            res += stack[i]
        return res
