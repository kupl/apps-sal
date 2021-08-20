class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        c = 1
        while self.stack and self.stack[-1][0] <= price:
            c += self.stack.pop()[1]
        self.stack.append([price, c])
        return c
