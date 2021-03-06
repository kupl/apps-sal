class StockSpanner:

    def __init__(self):
        self.st = []

    def next(self, price: int) -> int:
        sp = 1
        while self.st and self.st[-1][0] <= price:
            sp += self.st.pop()[1]
        self.st.append([price, sp])
        return sp
