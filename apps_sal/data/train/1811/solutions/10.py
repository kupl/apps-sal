class StockSpanner:

    def __init__(self):
        self.q = []

    def next(self, price: int) -> int:
        if not self.q or self.q[-1][0] > price:
            self.q.append((price, 1))
            return 1
        elif self.q and self.q[-1][0] == price:
            (c, l) = self.q.pop()
            self.q.append((price, l + 1))
            return l + 1
        elif self.q:
            level = 1
            while self.q and self.q[-1][0] <= price:
                (c, l) = self.q.pop()
                level += l
            self.q.append((price, level))
            return level
