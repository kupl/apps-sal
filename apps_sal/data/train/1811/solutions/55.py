class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        res = 1
        i = len(self.stack)
        while self.stack and self.stack[-1][0] <= price:
            (x, c) = self.stack.pop()
            res += c
        self.stack.append((price, res))
        return res
