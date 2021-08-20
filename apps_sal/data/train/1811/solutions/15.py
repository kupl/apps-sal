class StockSpanner:
    """
        [100, 80, 60, 70, 60, 75, 85]

        [100] -> (100, 0, 0)
        [100, 80] -> (100, 0, 0), (80, 1, 1)
        [100, 80, 60] -> (100, 0, 0), (80, 1, 1), (60, 2, 2)
        [100, 80, 60, 70] -> (100, 0, 0), (80, 1, 1), (70, 2, 3)
        [100, 80, 60, 70, 60] -> (100, 0, 0), (80, 1, 1), (70, 2, 3), (60, 4, 4)
        [100, 80, 60, 70, 60, 75] -> (100, 0, 0), (80, 1, 1), (75, 2, 5)
        [100, 80, 60, 70, 60, 75, 85] -> (100, 0, 0), (85, 1, 6)                
    """

    def __init__(self):
        self.stack = list()
        self.date = 0

    def next(self, price: int) -> int:
        (s, e) = (self.date, self.date)
        while len(self.stack) > 0 and self.stack[-1][0] <= price:
            s = self.stack[-1][1]
            self.stack.pop()
        self.stack.append([price, s])
        self.date += 1
        return e - s + 1
