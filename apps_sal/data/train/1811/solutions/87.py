class StockSpanner:

    def __init__(self):
        self.prices = []
        # left[i]: index of first price on the left > prices[i]
        self.left = []

    def next(self, price: int) -> int:
        cur = len(self.prices) - 1
        while cur >= 0 and self.prices[cur] <= price:
            cur = self.left[cur]
        
        self.left.append(cur)
        self.prices.append(price)
        return len(self.prices) - 1 - cur


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

