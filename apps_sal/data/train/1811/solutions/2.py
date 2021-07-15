class StockSpanner:

    def __init__(self):
        self.stack = []
        self.span = []

    def next(self, price: int) -> int:
        res = 1
        if not self.stack or price < self.stack[-1]:
            self.stack.append(price)
            self.span.append(1)
        else:
            while self.stack and price >= self.stack[-1]:
                self.stack.pop()
                res += self.span.pop()
            self.stack.append(price)
            self.span.append(res)
        return res

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

