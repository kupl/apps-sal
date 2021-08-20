"""
curr=0
[[inf,0]]

"""
from collections import deque


class StockSpanner:

    def __init__(self):
        self.stack = deque()
        self.counter = 0
        self.stack.append([float('inf'), 0])

    def update_stack(self, value):
        while value >= self.stack[len(self.stack) - 1][0]:
            self.stack.pop()

    def next(self, price: int) -> int:
        self.counter += 1
        self.update_stack(price)
        diff = abs(self.counter - self.stack[len(self.stack) - 1][1])
        self.stack.append([price, self.counter])
        return diff
