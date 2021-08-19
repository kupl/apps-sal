import math


class ProductOfNumbers:

    def __init__(self):
        self.l = []

    def add(self, num: int) -> None:
        self.l.append(num)

    def getProduct(self, k: int) -> int:
        return math.prod(self.l[len(self.l) - k:len(self.l)])
