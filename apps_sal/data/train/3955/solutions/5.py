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
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def bracket_pairs(s):
    l = len(s)
    stack = Stack()
    i = 0
    res = {}
    flag = True
    while i < l and flag:
        if s[i] == "(":
            stack.push(i)
        elif s[i] == ")":
            if stack.is_empty():
                flag = False
            else:
                a = stack.pop()
                res[a] = i
        i += 1
    if flag and stack.is_empty():
        return res
    return False
