class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = ['']
        for s in S:
            if s == stack[-1]:
                stack = stack[:-1]
            else:
                stack += [s]
        return ''.join(stack[1:])
