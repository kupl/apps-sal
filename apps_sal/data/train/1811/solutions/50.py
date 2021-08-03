class StockSpanner:

    def __init__(self):
        self.stocks = []
        self.spans = []

    def next(self, price: int) -> int:
        if not self.spans:
            self.spans.append(1)
            self.stocks.append(price)
            return 1
        elif price < self.stocks[-1]:
            self.spans.append(1)
            self.stocks.append(price)
            return 1
        else:
            newSpan = self.spans[-1]
            i = -1 * newSpan - 1
            while i >= -1 * len(self.stocks) and price >= self.stocks[i]:
                newSpan += 1
                i -= 1
            newSpan += 1
            self.spans.append(newSpan)
            self.stocks.append(price)
            return newSpan


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
