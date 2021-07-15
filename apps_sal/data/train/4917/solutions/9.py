import re

class Stack(object):
    def __init__(self): self._vals = []
    def push(self, i): self._vals.append(i)
    def peek(self): return self._vals[-1] if not self.is_empty() else None
    def pop(self): self._vals.pop()
    def is_empty(self): return len(self._vals) == 0

def validBraces(string):
    openers, closers = list(map(list, ('({[', ')}]')))
    pairs = list(zip(openers, closers))

    s = Stack()
    for char in list(string):
        if char in openers:
            s.push(char)
        elif (char in closers and (s.peek(), char) in pairs):
            s.pop()
    return s.is_empty()

