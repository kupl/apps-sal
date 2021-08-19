class ProductOfNumbers:

    def __init__(self):
        self.arr = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.arr = [1]
        else:
            self.arr.append(self.arr[-1] * num)

    def getProduct(self, k: int) -> int:
        if k > len(self.arr) - 1:
            return 0
        else:
            return int(self.arr[-1] / self.arr[-k - 1])
