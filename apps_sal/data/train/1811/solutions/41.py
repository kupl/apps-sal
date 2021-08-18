class StockSpanner:

    def __init__(self):
        self.prices = []
        self.lastP = 0
        self.lastCount = 0

    def next(self, price: int) -> int:
        if len(self.prices) == 0:

            self.lastCount = 1
            self.lastP = 0
            self.prices.append(price)
            return 1
        count = self.lastCount
        if price == self.prices[-1]:
            count += 1
            self.lastCount = count
        elif price > self.prices[-1]:
            count += 1
            isB = False
            for i in range(self.lastP - 1, -1, -1):
                if self.prices[i] <= price:
                    count += 1
                    self.lastP = i
                else:
                    isB = True
                    break
            if isB:
                self.lastP = i + 1
            else:
                self.lastP = 0
            self.lastCount = count
        elif price < self.prices[-1]:
            count = 1
            self.lastCount = count
            self.lastP = len(self.prices)
        self.prices.append(price)
        return count
