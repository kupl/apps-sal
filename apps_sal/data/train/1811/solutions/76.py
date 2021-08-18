class StockSpanner:

    def __init__(self):
        self.stacks = []

    def next(self, price: int) -> int:
        if len(self.stacks) == 0:
            self.stacks.append([price, 1])
            return 1
        else:
            p = 1
            while(len(self.stacks) > 0 and self.stacks[-1][0] <= price):
                ele = self.stacks.pop()
                p += ele[1]
            self.stacks.append([price, p])
            return p
