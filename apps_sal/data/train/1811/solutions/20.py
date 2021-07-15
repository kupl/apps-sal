class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        self.stack.append([price, 1])
        
        while len(self.stack) > 1 and self.stack[-1][0] >= self.stack[-2][0]:
            self.stack[-2][0] = self.stack[-1][0]
            self.stack[-2][1] += self.stack[-1][1]
            del self.stack[-1]
        return self.stack[-1][1]

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

