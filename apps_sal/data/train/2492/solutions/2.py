class Solution:

    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for line in logs:
            if line == '../':
                if stack:
                    stack.pop()
            elif line == './':
                pass
            else:
                stack.append(line)
        return len(stack)
