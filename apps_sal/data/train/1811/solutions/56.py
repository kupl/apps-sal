class StockSpanner:

    def __init__(self):
        self.stack = []
        self.num = 0
        self.stack.append((float('inf'), 0))

    def next(self, price: int) -> int:
        ret = 1
        self.num += 1
        while self.stack[-1][0] <= price:
            self.stack.pop()
        topIndex = self.stack[-1][1]
        self.stack.append((price, self.num))
        return self.num - topIndex
