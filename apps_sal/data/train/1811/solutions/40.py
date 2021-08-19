class StockSpanner:

    def __init__(self):
        self.stock = []  # a list that stores tuples (date_stock_price, span_start_index)

    def next(self, price: int) -> int:
        if not self.stock or (price < self.stock[-1][0]):
            span = 1
            self.stock.append((price, len(self.stock)))
        else:
            i = self.stock[-1][1] - 1
            while i >= 0 and self.stock[i][0] <= price:
                i -= 1
            span = len(self.stock) - i
            self.stock.append((price, i + 1))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
