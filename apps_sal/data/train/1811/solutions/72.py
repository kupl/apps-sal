class StockSpanner:

    def __init__(self):
        self.stock = []

    def next(self, price: int) -> int:
        val = 1
        while self.stock and self.stock[-1][0] <= price:
            val += self.stock.pop()[1]
        
        self.stock.append((price, val))
        return val


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

