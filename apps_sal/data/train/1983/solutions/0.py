import math
class ProductOfNumbers:

    def __init__(self):
        self.numbers = [1]
        self.lastZero = 0

    def add(self, num: int) -> None:
        if num != 0:
            self.numbers.append(self.numbers[-1] * num)
        else:
            self.numbers = [1]
            

    def getProduct(self, k: int) -> int:
        if k < len(self.numbers):
            return self.numbers[-1] // self.numbers[-k - 1]
        else:
            return 0


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

