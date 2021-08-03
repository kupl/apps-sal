class StockSpanner:

    def __init__(self):
        self.stack = []
        self.idx = 0
        self.stack.append((float(\"inf\"),0))
        

    def next(self, price: int) -> int:
        self.idx += 1
        while(self.stack and self.stack[-1][0] <= price):
            self.stack.pop()
        self.stack.append((price,self.idx))
        if(self.idx == 1):
            return 1
        else:
            return self.stack[-1][1] - self.stack[-2][1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
