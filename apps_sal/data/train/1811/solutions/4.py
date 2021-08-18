class StockSpanner:

    def __init__(self):
        self.stocks = []
        self.spans = []

    def next(self, price: int) -> int:
        self.stocks.append(price)
        self.spans.append(1)
        if len(self.stocks) == 1:
            return self.spans[0]
        idx = len(self.stocks) - 2
        cur_span = self.spans[-1]
        while(idx >= 0):
            if price < self.stocks[idx]:
                break
            else:
                cur_span += self.spans[idx]
                idx -= self.spans[idx]
        self.spans[-1] = cur_span
        return self.spans[-1]
