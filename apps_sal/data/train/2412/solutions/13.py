class Solution:
    def removeDuplicates(self, S: str) -> str:
        # stack application
        stack = []
        for i in S:
            if not stack:
                stack.append(i)
            elif i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)

        return ''.join(stack)
