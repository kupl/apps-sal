import math


class ProductOfNumbers:

    def __init__(self):
        self.arr = []

    def add(self, num: int) -> None:
        self.arr.append(num)

    def getProduct(self, k: int) -> int:
        return math.prod(self.arr[-k:])
