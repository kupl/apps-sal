class StockSpanner:

    def __init__(self):
        self.stack = []
        self.indx = -1
        self.results = []

    def next(self, price: int) -> int:
        self.indx += 1
        while len(self.stack) > 0 and self.stack[-1][1] <= price:
            self.stack.pop()
        if len(self.stack) == 0:
            self.stack.append([self.indx, price])
            return self.indx + 1
        result = self.stack[-1][0]
        self.stack.append([self.indx, price])
        return self.indx - result
