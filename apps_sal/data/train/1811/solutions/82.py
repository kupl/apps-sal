class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        weight = 1
        while self.stack != [] and price >= self.stack[-1][0]:
            weight += self.stack.pop()[1]
        self.stack.append((price, weight))
        return weight
