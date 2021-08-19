class StockSpanner:

    def __init__(self):
        self.s = []
        self.O = []

    def next(self, price: int) -> int:
        self.s.append(price)
        o = 0
        if len(self.s) == 1:
            self.O.append(1)
            return 1
        l = len(self.s)
        i = l - 2
        o = 1
        while i >= 0:
            if self.s[i] <= price:
                o += self.O[i]
                i -= self.O[i]
            else:
                break
        self.O.append(o)
        return o
