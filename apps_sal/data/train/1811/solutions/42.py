class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        result = 1
        while self.stack and self.stack[-1][0] <= price:
            previous_calculated_result = self.stack.pop()[1]
            result += previous_calculated_result
        self.stack.append([price, result])
        print(self.stack)
        return result
