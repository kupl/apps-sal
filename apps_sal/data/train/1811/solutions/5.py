'''
[100, 80, 60, 70, 60, 75, 85]
[1,    1,  1,  2,  1,  4,  6]
Assume that the span always has to include the current day.

Keep a stack of where spans start from left to right.
On a new price, pop elems from stack until the top is bigger than the current elem.
Then the top elem is the elem that ends the current day's span.



'''

class StockSpanner:

    def __init__(self):
        self.stack = list()
        self.ix = -1

    def next(self, price: int) -> int:
        self.ix += 1
        if not self.stack:
            self.stack.append((price, self.ix))
            return 1
        else:
            while self.stack and self.stack[-1][0] <= price:
                self.stack.pop()
            span_start = self.stack[-1][1] if self.stack else -1
            self.stack.append((price, self.ix))
            return self.ix - span_start


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

