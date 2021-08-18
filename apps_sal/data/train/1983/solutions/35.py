import math


class ProductOfNumbers:

    def __init__(self):
        self.numList = []

    def add(self, num: int) -> None:
        self.numList.append(num)

    def getProduct(self, k: int) -> int:
        prodList = self.numList[(-1 * k):]

        return math.prod(prodList)
