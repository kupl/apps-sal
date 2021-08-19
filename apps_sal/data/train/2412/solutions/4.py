class Solution:

    def removeDuplicates(self, S: str) -> str:
        if len(S) == 1:
            return S
        stack = []
        for i in range(len(S)):
            if len(stack) > 0 and stack[-1] == S[i]:
                stack.pop()
            else:
                stack.append(S[i])
        return ''.join(stack)
