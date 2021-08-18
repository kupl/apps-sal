class StockSpanner:

    def __init__(self):
        self.stocks = []
        self.topStocks = []

    def next(self, price: int) -> int:

        while(len(self.topStocks) > 0 and self.stocks[self.topStocks[-1]] <= price):
            self.topStocks.pop()
        flag = self.topStocks[-1] if len(self.topStocks) > 0 else -1
        self.topStocks.append(len(self.stocks))
        self.stocks.append(price)
        return len(self.stocks) - flag - 1
