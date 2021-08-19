import math


class ProductOfNumbers:

    def __init__(self):
        self.list = []

    def add(self, num: int) -> None:
        self.list.append(num)

    def getProduct(self, k: int) -> int:
        return math.prod(self.list[len(self.list) - k:])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
