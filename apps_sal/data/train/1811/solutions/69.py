class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        count = 1
        while self.stack and price >= self.stack[-1][0]:
            count += self.stack.pop()[1]
        self.stack.append((price, count))
        return count
