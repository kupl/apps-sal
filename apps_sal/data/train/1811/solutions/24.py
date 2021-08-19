class StockSpanner:

    def __init__(self):
        self.dp = []
        self.price = []

    def next(self, price: int) -> int:
        if len(self.price) == 0 or price < self.price[-1]:
            self.dp.append(1)
        else:
            i = len(self.price) - 1
            tmp = 1
            while price >= self.price[i] and i >= 0:
                tmp += self.dp[i]
                i -= self.dp[i]

            self.dp.append(tmp)

        self.price.append(price)
        return self.dp[-1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
