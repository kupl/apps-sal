class StockSpanner:

    def __init__(self):
        self.stack = []
        self.pre_less = []
        self.i = 0

    def next(self, price: int) -> int:
        self.i += 1
        while self.stack and self.stack[-1][1] <= price:
            self.stack.pop()

        result = None
        if not self.stack:
            result = self.i
        else:
            result = self.i - self.stack[-1][0]
        self.stack.append((self.i, price))
        return result


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
