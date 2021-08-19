class StockSpanner:

    def __init__(self):
        self.s = [float('inf')]
        self.pos = [0]
        self.num = 1

    def next(self, price: int) -> int:
        while self.s and self.s[-1] <= price:
            self.s.pop()
            self.pos.pop()
        r = self.num - self.pos[-1]
        self.s.append(price)
        self.pos.append(self.num)
        self.num += 1
        return r


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
