class StockSpanner:

    def __init__(self):
        self.arr = []

    def next(self, price: int) -> int:
        if len(self.arr) == 0:
            self.arr.append([price, 1])
            return 1

        i = len(self.arr) - 1
        count = 1
        while i >= 0 and price >= self.arr[i][0]:
            count += self.arr[i][1]
            i -= self.arr[i][1]

        self.arr.append([price, count])
        return count
