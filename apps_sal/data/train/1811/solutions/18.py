class StockSpanner:

    def __init__(self):
        self.idx = 0
        self.q = []

    def next(self, price: int) -> int:
        self.idx += 1
        if len(self.q) == 0 or self.q[-1][1] > price:
            self.q.append([self.idx, price])
            return 1
        else:
            while len(self.q) > 0 and self.q[-1][1] <= price:
                self.q.pop()
            if len(self.q) == 0:
                self.q.append([self.idx, price])
                return self.idx
            else:
                self.q.append([self.idx, price])
                return self.idx - self.q[-2][0]

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
