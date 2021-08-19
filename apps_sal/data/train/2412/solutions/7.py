class Solution:

    def removeDuplicates(self, S: str) -> str:
        stack = S[0]
        for i in range(1, len(S)):
            if len(stack) == 0:
                stack += S[i]
            elif stack and stack[-1] != S[i]:
                stack += S[i]
            elif stack:
                stack = stack[:-1]
        return stack
