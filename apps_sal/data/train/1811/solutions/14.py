class StockSpanner:

    def __init__(self):
        self._data = []

    def next(self, price: int) -> int:
        span = 1
        while self._data and self._data[-1][0] <= price:
            span += self._data.pop()[1]

        self._data.append((price, span))
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

