class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def solve(s):
    l = len(s)
    if l % 2 != 0:
        return -1
    stack = Stack()
    count = 0
    i = 0
    while i < len(s):
        if s[i] == '(':
            stack.push(s[i])
        elif stack.is_empty():
            count += 1
        else:
            stack.pop()
        i += 1
    q = (count + stack.size()) // 2
    return q if count % 2 == 0 and stack.size() % 2 == 0 else q + 1
