class StockSpanner:

    def __init__(self):
        self.s = list()

    def next(self, price: int) -> int:
        weight = 1
        stack = self.s
        while(stack and stack[-1][0] <= price):
            weight += stack[-1][-1]
            stack.pop()
        stack.append((price, weight))
        return weight


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
