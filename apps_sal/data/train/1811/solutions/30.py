from collections import OrderedDict


class StockSpanner(OrderedDict):

    def __init__(self):
        self.counts = 0

    def next(self, price: int) -> int:
        i = len(self) - 1
        idx = self.counts
        items = list(self.items())
        while i >= 0 and items[i][0] <= price:
            idx = self[items[i][0]]
            self.popitem(last=True)
            i -= 1
        self[price] = idx
        self.counts += 1
        return self.counts - idx


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
