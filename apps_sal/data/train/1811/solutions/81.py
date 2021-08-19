class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        idx = 1
        while self.stack and self.stack[-1][0] <= price:
            idx += self.stack.pop()[1]
        self.stack.append([price, idx])
        return idx


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
