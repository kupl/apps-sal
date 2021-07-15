class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        weight = 1
        while self.stack and self.stack[-1][0] <= price:
            _, currentWeight = self.stack.pop()
            weight += currentWeight
        self.stack.append((price, weight))
        return weight
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

