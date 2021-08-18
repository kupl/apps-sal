class StockSpanner:

    def __init__(self):
        self.st = []

    def next(self, price):
        span = 1
        while (len(self.st) > 0) and self.st[-1][0] <= price:
            span = span + self.st[-1][1]
            self.st.pop()
        self.st.append((price, span))
        return span
