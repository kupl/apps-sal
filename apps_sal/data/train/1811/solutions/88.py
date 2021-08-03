class StockSpanner:

    def __init__(self):
        self.prices = []
        self.decreasing_stack = []

    def next(self, price: int) -> int:
        while self.decreasing_stack and self.prices[self.decreasing_stack[-1]] <= price:
            self.decreasing_stack.pop()
        ret = len(self.prices) - self.decreasing_stack[-1] if self.decreasing_stack else len(self.prices) + 1
        self.decreasing_stack.append(len(self.prices))
        self.prices.append(price)
        return ret


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
