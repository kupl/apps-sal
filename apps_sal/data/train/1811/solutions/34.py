
class StockSpanner:

    def __init__(self):
        self.prices = []
        self.spans = []

    def next(self, price: int) -> int:
        self.prices.append(price)
        value = 1
        index = len(self.spans) - 1
        while(index >= 0):
            if self.prices[index] <= price:
                value += self.spans[index]
                index -= self.spans[index]
            else:
                break
        self.spans.append(value)
        return value
