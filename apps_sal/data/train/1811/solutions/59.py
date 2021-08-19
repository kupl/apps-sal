class StockSpanner:

    def __init__(self):
        self.priceList = []
        self.n = 0
        self.prevSpan = 0
        self.curSpan = 0

    def next(self, price: int) -> int:
        if not self.priceList:
            self.priceList.append(price)
            self.n += 1
            self.curSpan = 1
            self.prevSpan = self.curSpan
            return self.curSpan
        prev = self.priceList[-1]
        self.priceList.append(price)
        self.n += 1
        if price < prev:
            self.curSpan = 1
            self.prevSpan = self.curSpan
            return self.curSpan
        else:
            self.curSpan = 1 + self.prevSpan
            i = self.n - self.curSpan - 1
            # if i >= 0:
            #     cur = priceList[i]
            while i >= 0 and self.priceList[i] <= price:
                self.curSpan += 1
                i = self.n - self.curSpan - 1
            self.prevSpan = self.curSpan
            return self.curSpan


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
