class StockSpanner:

    def __init__(self):
        self.stack = []
        self.i = 0

    def next(self, price: int) -> int:
        while self.stack and self.stack[-1][1] <= price:
            self.stack.pop()
        index = self.stack[-1][0] if self.stack else -1
        diff = self.i - index
        self.stack.append((self.i, price))
        self.i += 1
        return diff
