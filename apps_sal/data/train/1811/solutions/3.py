class StockSpanner:

    def __init__(self):
        self.st = []

    def next(self, price: int) -> int:
        cnt = 1
        while self.st and price >= self.st[-1][0]:
            cnt += self.st.pop()[1]
        self.st.append((price, cnt))
        print((self.st))
        return cnt


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
