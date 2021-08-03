class Item:
    def __init__(self, value, index):
        self.value = value
        self.index = index


class Stack:
    def __init__(self):
        self._stack = []
        self._top_index = 0

    def top(self):
        if self._top_index <= 0:
            return None
        return self._stack[self._top_index - 1]

    def pop(self):
        item = self._stack.pop()
        self._top_index -= 1
        return item

    def push(self, item):
        self._stack.append(item)
        self._top_index += 1

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self._stack):
            raise StopIteration
        value = self._stack[self.index]
        self.index += 1
        return value


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = Stack()

        for index, c in enumerate(s):
            if c == '(':
                item = Item('(', index)
                stack.push(item)
            elif c == ')':
                if stack.top() and stack.top().value == '(':
                    stack.pop()
                else:
                    item = Item(')', index)
                    stack.push(item)

        prev_index = 0
        result = ''
        for item in stack:
            result += s[prev_index:item.index]
            prev_index = item.index + 1
        result += s[prev_index:]

        return result
