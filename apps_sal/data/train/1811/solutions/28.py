class StockSpanner:

    def __init__(self):
        self.stack = []
        self.uid = 1

    def next(self, price):
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        if self.stack:
            res = self.uid - self.stack[-1][1]
        else:
            res = self.uid
        self.stack.append([price, self.uid])
        self.uid += 1
        return res
