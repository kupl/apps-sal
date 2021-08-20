class StockSpanner:

    def __init__(self):
        self.spanStk = []

    def next(self, price: int) -> int:
        if len(self.spanStk) == 0:
            self.spanStk.append((price, 1))
        else:
            new_weight = 1
            while len(self.spanStk) != 0 and self.spanStk[-1][0] <= price:
                new_weight += self.spanStk[-1][1]
                self.spanStk.pop()
            self.spanStk.append((price, new_weight))
        return self.spanStk[-1][1]
