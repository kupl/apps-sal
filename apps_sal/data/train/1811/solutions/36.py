import bisect


class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        total = 1
        while self.stack and self.stack[-1][0] <= price:
            total += self.stack.pop()[1]
        self.stack.append((price, total))
        return total
