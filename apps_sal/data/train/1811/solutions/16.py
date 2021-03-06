class StockSpanner:

    def __init__(self):
        self.cur = -1
        self.stack = []
        self.prices = {}

    def next(self, price: int) -> int:
        self.cur += 1
        self.prices[self.cur] = price
        while self.stack and self.prices[self.stack[-1]] <= price:
            self.prices.pop(self.stack.pop())
        res = self.cur - self.stack[-1] if self.stack else self.cur + 1
        self.stack.append(self.cur)
        return res
