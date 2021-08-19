class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        cnt = 1
        while self.stack and self.stack[-1][0] <= price:
            (p, c) = self.stack.pop()
            cnt += c
        self.stack.append([price, cnt])
        return cnt
