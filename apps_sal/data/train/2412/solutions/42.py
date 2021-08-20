class Solution:

    def removeDuplicates(self, S: str) -> str:
        stack = []
        for elem in S:
            if stack == []:
                stack.append(elem)
            elif stack[-1] == elem:
                stack = stack[:-1]
            else:
                stack.append(elem)
        return ''.join(stack)
