class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        count = 1
        while self.stack and price >= self.stack[-1][0]:
            count += self.stack[-1][1]
            del self.stack[-1]
        self.stack.append([price, count])
        return self.stack[-1][1]
