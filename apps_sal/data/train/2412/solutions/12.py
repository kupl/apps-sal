class Solution:
    def removeDuplicates(self, S: str) -> str:
        if not S:
            return None
        stack = []
        for s in S:
            if len(stack) > 0 and s == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([s, 1])
            if stack[-1][1] == 2:
                stack.pop()
        return ''.join(char * num for char, num in stack)
