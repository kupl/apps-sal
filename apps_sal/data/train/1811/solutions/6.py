class StockSpanner:

    def __init__(self):
        self.history = []
        self.output = []

    def next(self, price: int) -> int:
        less_than_count = 1
        while self.history and self.history[-1][0] <= price:
            less_than_count += self.history.pop()[1]
        self.output.append(less_than_count)
        self.history.append((price, less_than_count))
        return self.output[-1]
