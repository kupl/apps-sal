class StockSpanner:

    def __init__(self):
        self.stack = []
        self.cnt = 0

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append((price, 1))
            return 1
        else:
            cnt_removed = 1
            while self.stack and self.stack[-1][0] <= price:
                node = self.stack.pop()
                cnt_removed += node[1]
            self.stack.append((price, cnt_removed))
            if cnt_removed > 1:
                return cnt_removed
            else:
                return 1
