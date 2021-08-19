class StockSpanner:

    def __init__(self):
        self.stack = []
        self.len = -2

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append([price, 1])
            return 1
        ans = 0
        while self.stack and self.stack[-1][0] <= price:
            elm = self.stack.pop()
            ans += elm[1]
        self.stack.append([price, ans + 1])
        return ans + 1
