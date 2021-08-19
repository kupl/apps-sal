class StockSpanner:

    def __init__(self):
        self.prices = []
        self.left = []

    def next(self, price: int) -> int:
        cur = len(self.prices) - 1
        while cur >= 0 and self.prices[cur] <= price:
            cur = self.left[cur]
        self.left.append(cur)
        self.prices.append(price)
        return len(self.prices) - 1 - cur
