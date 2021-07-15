class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        # while there is a stack and the top of the stack(aka the previous values) has a value that's less than or equal to the current price
        while self.stack and self.stack[-1][0] <= price: 
            span = span + self.stack.pop()[1]  # update the span
        self.stack.append([price, span])
    
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

