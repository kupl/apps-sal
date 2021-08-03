class StockSpanner:

    def __init__(self):
        self.monotone_stack = []

    def next(self, price: int) -> int:
        stack = self.monotone_stack
        current_price, current_span = price, 1
        while stack and stack[-1][0] <= current_price:
            pre_price, pre_span = stack.pop()
            current_span += pre_span
        stack.append((current_price, current_span))

        return current_span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
