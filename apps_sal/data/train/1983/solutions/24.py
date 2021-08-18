import math


class ProductOfNumbers:

    def __init__(self):
        self.list = []

    def add(self, num: int) -> None:
        self.list.append(num)

    def getProduct(self, k: int) -> int:
        return math.prod(self.list[len(self.list) - k:])
