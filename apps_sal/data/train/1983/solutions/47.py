

class ProductOfNumbers:

    def __init__(self):
        self.arr = [1]
        self.zero = -1

    def add(self, num: int) -> None:

        if num == 0:
            self.arr.append(self.arr[-1])
            self.zero = len(self.arr) - 1
        else:
            self.arr.append(self.arr[-1] * num)

    def getProduct(self, k: int) -> int:

        if self.zero != -1 and self.zero >= len(self.arr) - k:
            return 0

        return self.arr[-1] // self.arr[-k - 1]
