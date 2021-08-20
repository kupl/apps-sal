class Stack:
    """
    This is an implementation of a Stack.
    The "right" or "top" of this stack the end of the list.
    """

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


def valid_parentheses(symbol_string):
    """
    This is a practice problem.
    It checks to see if parenthesis's are balanced
    :param symbol_string: String
    :return Bool:
    """
    stack = Stack()
    for char in symbol_string:
        if char == '(':
            stack.push('(')
        elif char == ')':
            if stack.is_empty():
                return False
            else:
                stack.pop()
    if not stack.is_empty():
        return False
    else:
        return True
