class StockSpanner:

    def __init__(self):
        self.stock = []

    def next(self, price: int) -> int:
        if not self.stock or price < self.stock[-1][0]:
            span = 1
            self.stock.append((price, len(self.stock)))
        else:
            i = self.stock[-1][1] - 1
            while i >= 0 and self.stock[i][0] <= price:
                i -= 1
            span = len(self.stock) - i
            self.stock.append((price, i + 1))
        return span
