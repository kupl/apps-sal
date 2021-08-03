class StockSpanner:

    def __init__(self):
        self.stack = [[float('inf'), -1]]
        self.idx = 0

    def next(self, price: int) -> int:
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        ans = self.idx - self.stack[-1][1]
        self.stack.append([price, self.idx])
        self.idx += 1
        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
