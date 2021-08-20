class StockSpanner:

    def __init__(self):
        self.stack = [[0, 1]]

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append([price, 1])
            return 1
        elif self.stack and price < self.stack[-1][0]:
            self.stack.append([price, 1])
            return 1
        else:
            days = 0
            while self.stack and price >= self.stack[-1][0]:
                (p, d) = self.stack.pop()
                days += d
            try:
                days += self.stack[-1][1]
                self.stack[-1][1] = days
            except:
                self.stack.append([0, days])
            self.stack.append([price, 1])
            print(self.stack)
        return days
