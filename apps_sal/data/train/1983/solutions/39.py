import math


class ProductOfNumbers:

    def __init__(self):
        self.numbers = []

    def add(self, num: int) -> None:
        self.numbers.append(num)

    def getProduct(self, k: int) -> int:
        return math.prod(self.numbers[-k:])
