class Solution:
    def removeDuplicates(self, string: str) -> str:
        stack = deque()
        stack.append(string[0])
        index = 0
        for i in range(1, len(string)):
            stack.append(string[i])
            index += 1
            if stack[index] == stack[index - 1] and len(stack) > 1:
                for i in range(2):
                    if stack:
                        stack.pop()
                        index -= 1
        s = ''
        for i in range(len(stack)):
            s += stack[i]
        return (s)
