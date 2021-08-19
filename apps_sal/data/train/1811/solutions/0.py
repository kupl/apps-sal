class StockSpanner:

    def __init__(self):
        self.s = []

    def next(self, price: int) -> int:
        stk = self.s
        curr_span = 1
        while stk and stk[-1][0] <= price:
            (prev_price, prev_span) = stk.pop()
            curr_span += prev_span
        stk.append((price, curr_span))
        return curr_span
