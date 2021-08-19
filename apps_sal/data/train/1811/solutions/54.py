class StockSpanner:

    def __init__(self):
        self.monotone_stack = []

    def next(self, price: int) -> int:
        stack = self.monotone_stack
        (cur_price_quote, cur_price_span) = (price, 1)
        while stack and stack[-1][0] <= cur_price_quote:
            (prev_price_quote, prev_price_span) = stack.pop()
            cur_price_span += prev_price_span
        stack.append((cur_price_quote, cur_price_span))
        return cur_price_span
