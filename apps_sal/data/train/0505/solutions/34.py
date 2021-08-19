class Stack:

    def __init__(self):
        self.stack = collections.deque()

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def empty(self):
        try:
            item = self.stack.pop()
            self.stack.append(item)
            return False
        except IndexError:
            return True


class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        stack = Stack()
        remove_indices = []
        for (i, char) in enumerate(s):
            if char == '(':
                stack.push(i)
            if char == ')':
                if stack.empty():
                    remove_indices.append(i)
                else:
                    stack.pop()
        while not stack.empty():
            remove_indices.append(stack.pop())
        res = ''
        j = 0
        for i in range(len(s)):
            if j < len(remove_indices):
                if i not in remove_indices:
                    res += s[i]
                else:
                    j += 1
            else:
                res += s[i]
        return res
